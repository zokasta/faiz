from docx2pdf import convert
from .utils import get_output_path
from pathlib import Path

def word_to_pdf(docx_file):
    output_pdf = get_output_path(docx_file, f"{Path(docx_file).stem}.pdf")
    try:
        convert(docx_file, output_pdf)
        print(f"✅ Converted to PDF: {output_pdf}")
    except Exception as e:
        print(f"❌ Conversion failed: {e}")
