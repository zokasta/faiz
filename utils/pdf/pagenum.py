from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path
from .utils import get_output_path  # ✅ Import the utility

def main(args):
    if not args:
        print("❗ Usage: pagenum <file.pdf> [--output name]")
        return

    file = args[0]
    output_name = args[args.index('--output')+1] if '--output' in args else f"pagenum_{Path(file).name}"

    if not Path(file).is_file():
        print("❌ File not found.")
        return

    try:
        reader = PdfReader(file)
        writer = PdfWriter()
        for i, page in enumerate(reader.pages):
            writer.add_page(page)
            writer.add_metadata({f"/PageLabel_{i+1}": f"{i+1}"})

        out_path = get_output_path(file, output_name)  # ✅ Use helper here
        with open(out_path, "wb") as f:
            writer.write(f)
        print(f"🔢 Page numbered PDF saved as: {out_path}")
    except Exception as e:
        print(f"❌ Page numbering failed: {e}")
