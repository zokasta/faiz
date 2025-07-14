from PIL import Image
from .utils import get_output_path

def images_to_pdf(image_paths, output_name="images.pdf"):
    output_file = get_output_path(image_paths[0], output_name)
    try:
        imgs = [Image.open(img).convert("RGB") for img in image_paths]
        imgs[0].save(output_file, save_all=True, append_images=imgs[1:])
        print(f"✅ Images converted to PDF: {output_file}")
    except Exception as e:
        print(f"❌ Image to PDF failed: {e}")
