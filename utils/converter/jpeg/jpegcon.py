import os
import glob
import time
from PIL import Image, ExifTags
import pillow_heif
from concurrent.futures import ThreadPoolExecutor
import threading
from ..utils.checker import isImage
pillow_heif.register_heif_opener()

OUTPUT_DIR = "converted_jpeg"
lock = threading.Lock()

stats = {
    "total_images": 0,
    "converted": 0,
    "failed": 0,
    "start_time": None
}

\
def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def fix_orientation(img):
    try:
        for orientation_tag in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation_tag] == 'Orientation':
                break
        exif = img._getexif()
        if exif is not None:
            orientation = exif.get(orientation_tag, None)
            if orientation == 3:
                img = img.rotate(180, expand=True)
            elif orientation == 6:
                img = img.rotate(270, expand=True)
            elif orientation == 8:
                img = img.rotate(90, expand=True)
    except Exception:
        pass
    return img

def format_size(bytes_size):
    return f"{bytes_size / (1024 * 1024):.2f} MB" if bytes_size > 1024 * 1024 else f"{bytes_size / 1024:.2f} KB"

def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.0f} sec"
    else:
        minutes = int(seconds // 60)
        sec = int(seconds % 60)
        return f"{minutes} min {sec} sec"

def convert_single_image(img_path, total):
    global stats
    try:
        start = time.time()
        with Image.open(img_path) as img:
            img = fix_orientation(img)
            base_name = os.path.splitext(os.path.basename(img_path))[0]
            output_path = os.path.join(OUTPUT_DIR, base_name + ".jpeg")

            input_size = os.path.getsize(img_path)
            img.convert("RGB").save(output_path, "JPEG")
            output_size = os.path.getsize(output_path)
            reduction = 100 * (input_size - output_size) / input_size if input_size else 0

            elapsed = time.time() - start

            with lock:
                stats["converted"] += 1
                index = stats["converted"] + stats["failed"]

            print(f"[{index}/{total}] ✅ {os.path.basename(img_path)}")
            print(f"    ⏹ Before:  {format_size(input_size)}")
            print(f"    🟢 After:   {format_size(output_size)}")
            print(f"    📉 Reduced: {reduction:.2f}%")
            print(f"    ⏱️ Time:     {format_time(elapsed)}\n")

    except Exception as e:
        with lock:
            stats["failed"] += 1
            index = stats["converted"] + stats["failed"]
        print(f"[{index}/{total}] ❌ Failed: {os.path.basename(img_path)} ({e})")

def process_images(image_paths):
    stats["start_time"] = time.time()
    stats["total_images"] = len(image_paths)
    ensure_output_dir()

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(convert_single_image, img, len(image_paths)) for img in image_paths]
        for future in futures:
            future.result()

    print_summary()

def print_summary():
    total_time = time.time() - stats["start_time"]
    print("\n📊 Conversion Summary")
    print("=" * 40)
    print(f"🖼️  Total Images:       {stats['total_images']}")
    print(f"✅ Converted:          {stats['converted']}")
    print(f"❌ Failed:             {stats['failed']}")
    print(f"⏱️  Total Time:        {format_time(total_time)}")
    print("=" * 40)

def convert_to_jpeg(args):
    if not args:
        print("Usage: faiz jpeg <file|pattern|*>")
        return

    pattern = args[0]
    ensure_output_dir()

    if "*" in pattern:
        candidates = glob.glob(pattern)
    elif os.path.isfile(pattern):
        candidates = [pattern]
    else:
        candidates = os.listdir()

    image_files = [f for f in candidates if isImage(f)]

    if not image_files:
        print("❌ No images found.")
        return

    print(f"🔄 Converting {len(image_files)} images to JPEG...")
    process_images(image_files)

def main(args):
    convert_to_jpeg(args)
