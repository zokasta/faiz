from pdf2image import convert_from_path
from .utils import get_output_path
from pathlib import Path


def pdf_to_images(pdf_path):
    try:
        images = convert_from_path(pdf_path)
        for i, img in enumerate(images):
            img_path = get_output_path(pdf_path, f"{Path(pdf_path).stem}_page_{i+1}.jpg")
            img.save(img_path, "JPEG")
            print(f"🖼️ Saved: {img_path}")
    except Exception as e:
        print(f"❌ PDF to Image failed: {e}")

