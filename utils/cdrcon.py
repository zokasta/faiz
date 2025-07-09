import os
import sys
import glob
from concurrent.futures import ThreadPoolExecutor
import cairosvg

# Output directory for converted files
OUTPUT_DIR = "converted_pdf"

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def convert_svg_to_pdf(input_path, output_path=None, batch_mode=False):
    try:
        if not os.path.exists(input_path):
            print(f"❌ File not found: {input_path}")
            return

        if output_path is None:
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            if batch_mode:
                output_path = os.path.join(OUTPUT_DIR, base_name + ".pdf")
            else:
                output_path = os.path.join(os.path.dirname(input_path), base_name + ".pdf")

        cairosvg.svg2pdf(url=input_path, write_to=output_path)
        print(f"✅ Converted: {input_path} -> {output_path}")

    except Exception as e:
        print(f"❌ Error converting {input_path}: {e}")

def process_svg_files(image_files):
    ensure_output_dir()
    with ThreadPoolExecutor() as executor:
        executor.map(lambda f: convert_svg_to_pdf(f, batch_mode=True), image_files)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cdrcon.py <svg_file_or_pattern>")
        sys.exit(1)

    input_pattern = sys.argv[1]

    if "*" in input_pattern:
        image_files = glob.glob(input_pattern)
        if not image_files:
            print("❌ No matching files found.")
        else:
            print(f"🔄 Processing {len(image_files)} SVG files in parallel...")
            process_svg_files(image_files)
    else:
        input_path = input_pattern
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        convert_svg_to_pdf(input_path, output_path, batch_mode=False)
