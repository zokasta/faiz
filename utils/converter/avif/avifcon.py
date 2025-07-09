import os
import sys
import glob
import shutil
import subprocess
import signal
import time
from ..utils.checker import isImage  # ✅ Import isImage

OUTPUT_DIR = "converted_avif"
FAILED_DIR = "failed_avif"

# Stats tracking
stats = {
    "total_images": 0,
    "converted": 0,
    "skipped": 0,
    "failed": 0,
    "total_input_size": 0,
    "total_output_size": 0,
    "start_time": None
}

should_stop = False  # Graceful stop flag


def format_size(bytes_size):
    return f"{bytes_size / (1024 * 1024):.2f} MB" if bytes_size >= 1024 * 1024 else f"{bytes_size / 1024:.2f} KB"


def signal_handler(sig, frame):
    global should_stop
    should_stop = True
    print("\n🛑 Interrupted! Finishing remaining stats...\n")
    print_summary()
    sys.exit(0)


def ensure_dirs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(FAILED_DIR, exist_ok=True)


def convert_to_avif(input_path, output_path=None, batch_mode=False, retries=3, index=None, total=None):
    global stats

    if should_stop:
        return

    # ✅ Check if file is an image
    if not isImage(input_path):
        print(f"[{index}/{total}] ⏩ Skipped (not an image): {input_path}")
        stats["skipped"] += 1
        return

    if not os.path.exists(input_path):
        print(f"❌ Error: File not found - {input_path}")
        stats["skipped"] += 1
        return

    if output_path is None:
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_path = os.path.join(OUTPUT_DIR if batch_mode else os.path.dirname(input_path), base_name + ".avif")

    input_size = os.path.getsize(input_path)
    stats["total_input_size"] += input_size

    attempt = 0
    while attempt < retries:
        try:
            command = [
                "ffmpeg",
                "-y",
                "-i", input_path,
                "-c:v", "libaom-av1",
                "-crf", "30",
                "-b:v", "0",
                output_path
            ]
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            if not os.path.exists(output_path):
                raise RuntimeError("⚠️ FFmpeg ran, but output file is missing.")

            output_size = os.path.getsize(output_path)
            stats["total_output_size"] += output_size
            stats["converted"] += 1

            reduction = 100 * (input_size - output_size) / input_size if input_size else 0
            print(f"[{index}/{total}] ✅ Converted: {os.path.basename(input_path)}")
            print(f"    ⏹ Before:  {format_size(input_size)}")
            print(f"    🟢 After:   {format_size(output_size)}")
            print(f"    📉 Reduced: {reduction:.2f}%\n")
            return
        except subprocess.CalledProcessError:
            attempt += 1
            print(f"⚠️ Attempt {attempt} failed for {input_path}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            break

    print(f"❌ Giving up on: {input_path}")
    stats["failed"] += 1
    try:
        shutil.copy2(input_path, os.path.join(FAILED_DIR, os.path.basename(input_path)))
        print(f"📁 Copied to failed folder: {input_path}")
    except Exception as e:
        print(f"❌ Failed to copy to failed folder: {e}")


def process_images(image_files):
    stats["start_time"] = time.time()
    ensure_dirs()
    total = len(image_files)
    stats["total_images"] = total

    for idx, file in enumerate(image_files, start=1):
        if should_stop:
            break
        convert_to_avif(file, batch_mode=True, index=idx, total=total)

    print_summary()


def print_summary():
    duration = time.time() - stats["start_time"]
    total_in = stats["total_input_size"]
    total_out = stats["total_output_size"]
    total_saved = total_in - total_out
    avg_in = total_in / stats["converted"] if stats["converted"] else 0
    avg_out = total_out / stats["converted"] if stats["converted"] else 0
    avg_reduction = 100 * (avg_in - avg_out) / avg_in if avg_in else 0

    print("\n📊 Conversion Summary")
    print("===========================")
    print(f"🖼️  Total Images:         {stats['total_images']}")
    print(f"✅ Successfully Converted: {stats['converted']}")
    print(f"⏩ Skipped:               {stats['skipped']}")
    print(f"❌ Failed:                {stats['failed']}")
    print(f"⏱️  Total Time:           {duration:.2f} seconds")
    if stats["converted"]:
        print(f"\n📦 Size Summary:")
        print(f"📥 Total Before:         {format_size(total_in)}")
        print(f"📤 Total After:          {format_size(total_out)}")
        print(f"📉 Total Saved:          {format_size(total_saved)}")
        print(f"⚖️  Avg Before:           {format_size(avg_in)}")
        print(f"⚖️  Avg After:            {format_size(avg_out)}")
        print(f"🔻 Avg Reduction:         {avg_reduction:.2f}%")
    print("===========================\n")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    if len(sys.argv) < 2:
        print("Usage: python convert_to_avif.py <image_path_or_glob_pattern>")
    else:
        input_pattern = sys.argv[1]

        if "*" in input_pattern:
            image_files = glob.glob(input_pattern)
            if not image_files:
                print("❌ No matching files found.")
            else:
                print(f"🔄 Processing {len(image_files)} images...")
                process_images(image_files)
        else:
            input_path = input_pattern
            output_path = sys.argv[2] if len(sys.argv) > 2 else None
            stats["start_time"] = time.time()
            convert_to_avif(input_path, output_path, batch_mode=False, index=1, total=1)
            print_summary()
