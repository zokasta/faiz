from pdf2docx import Converter
from .utils import get_output_path
from pathlib import Path

def pdf_to_word(pdf_file):
    docx_file = get_output_path(pdf_file, f"{Path(pdf_file).stem}.docx")
    try:
        cv = Converter(pdf_file)
        cv.convert(docx_file, start=0, end=None)
        cv.close()
        print(f"✅ Converted to Word: {docx_file}")
    except Exception as e:
        print(f"❌ Conversion failed: {e}")
