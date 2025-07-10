import os

def isImage(filename):
    image_exts = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".avif"}
    ext = os.path.splitext(filename)[1].lower() 
    return ext in image_exts
