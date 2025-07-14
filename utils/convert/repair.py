from PyPDF2 import PdfReader, PdfWriter
from .utils import get_output_path
from pathlib import Path

def repair_pdf(file_path):
    output = get_output_path(file_path, f"repaired_{Path(file_path).name}")
    try:
        reader = PdfReader(file_path, strict=False)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        with open(output, 'wb') as f:
            writer.write(f)
        print(f"🔧 Repaired PDF saved as: {output}")
    except Exception as e:
        print(f"❌ Repair failed: {e}")
