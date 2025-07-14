from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from .utils import get_output_path  # ✅ Import the utility

def rotate_pdf(file_path, angle, output=None):
    "🔃 Rotate all pages in a PDF."
    if not Path(file_path).is_file():
        print("❌ File not found.")
        return
    try:
        reader = PdfReader(file_path)
        writer = PdfWriter()
        for page in reader.pages:
            page.rotate(int(angle))
            writer.add_page(page)

        output_name = output or f"rotated_{Path(file_path).name}"
        out_path = get_output_path(file_path, output_name)  # ✅ Use utility

        with open(out_path, 'wb') as f:
            writer.write(f)
        print(f"🔃 Rotated PDF saved as: {out_path}")
    except Exception as e:
        print(f"❌ Rotate failed: {e}")
