import os

def isImage(file_path):
    image_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.heic', '.bmp', '.tiff', '.gif', '.avif')
    return file_path.lower().endswith(image_extensions) and os.path.isfile(file_path)
