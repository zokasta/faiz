from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from .utils import get_output_path  # ✅ Import utility

def split_pdf(file_path):
    "✂️ Split a PDF into individual pages."
    if not Path(file_path).is_file():
        print("❌ File not found.")
        return

    try:
        reader = PdfReader(file_path)
        for i, page in enumerate(reader.pages, 1):
            writer = PdfWriter()
            writer.add_page(page)
            output_name = f"{Path(file_path).stem}_page_{i}.pdf"
            out_path = get_output_path(file_path, output_name)  # ✅ Use utility
            with open(out_path, 'wb') as f:
                writer.write(f)
            print(f"📄 Page {i} saved as: {out_path}")
    except Exception as e:
        print(f"❌ Split failed: {e}")
