import pdfkit
from .utils import get_output_path
from pathlib import Path

def html_to_pdf(html_file):
    output_pdf = get_output_path(html_file, f"{Path(html_file).stem}.pdf")
    try:
        pdfkit.from_file(html_file, output_pdf)
        print(f"✅ HTML converted to PDF: {output_pdf}")
    except Exception as e:
        print(f"❌ HTML to PDF failed: {e}")

