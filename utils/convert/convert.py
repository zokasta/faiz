import sys
from pathlib import Path
from .pdf2word import pdf_to_word
from .word2pdf import word_to_pdf
from .img2pdf import images_to_pdf
from .pdf2img import pdf_to_images
from .html2pdf import html_to_pdf
from .repair import repair_pdf

def show_help():
    print("""
🛠️  Available Conversions:
===========================
👉 pdf2word <file.pdf>
👉 word2pdf <file.docx>
👉 img2pdf <img1> <img2> ...
👉 pdf2img <file.pdf>
👉 html2pdf <file.html>
👉 repair <file.pdf>

Example:
    faiz convert pdf2word resume.pdf
    faiz convert word2pdf report.docx
    faiz convert img2pdf img1.jpg img2.jpg
===========================
""")

def main(args):
    if not args:
        show_help()
        return

    cmd = args[0]
    files = args[1:]

    if cmd == "pdf2word" and files:
        pdf_to_word(files[0])
    elif cmd == "word2pdf" and files:
        word_to_pdf(files[0])
    elif cmd == "img2pdf" and files:
        images_to_pdf(files)
    elif cmd == "pdf2img" and files:
        pdf_to_images(files[0])
    elif cmd == "html2pdf" and files:
        html_to_pdf(files[0])
    elif cmd == "repair" and files:
        repair_pdf(files[0])
    else:
        print(f"❌ Unknown or incomplete convert command: {' '.join(args)}")
        show_help()
