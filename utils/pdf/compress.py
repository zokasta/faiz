from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path
from .utils import get_output_path  # 👈 Import the helper

def main(args):
    if not args:
        print("❗ Usage: compress <file.pdf> [--output name]")
        return

    file = args[0]
    default_name = f"compressed_{Path(file).name}"
    output_name = args[args.index('--output') + 1] if '--output' in args else default_name
    output_path = get_output_path(file, output_name)  # 👈 Use the utility here

    try:
        reader = PdfReader(file)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        with open(output_path, 'wb') as f:
            writer.write(f)
        print(f"📦 Compressed PDF saved as: {output_path}")
    except Exception as e:
        print(f"❌ Compress failed: {e}")
