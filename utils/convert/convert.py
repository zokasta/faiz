import sys
from pathlib import Path
from .pdf2word import pdf_to_word
from .word2pdf import word_to_pdf
from .img2pdf import images_to_pdf
from .pdf2img import pdf_to_images
from .html2pdf import html_to_pdf
from .vidtomp3 import video_to_mp3


def show_help():
    print("""
🛠️  Available Conversions:
===========================
👉 pdf2word | pdftoword <file.pdf>
👉 word2pdf | wordtopdf <file.docx>
👉 img2pdf  | imagetopdf <img1> <img2> ...
👉 pdf2img  | pdftojpg <file.pdf>
👉 vid2mp3  | vidtomp3 <file.pdf>
👉 html2pdf <file.html>

Examples:
    faiz convert pdf2word resume.pdf
    faiz convert word2pdf report.docx
    faiz convert img2pdf img1.jpg img2.jpg
===========================
""")

def main(args):
    if not args:
        show_help()
        return

    cmd = args[0].lower()
    files = args[1:]

    match cmd:
        case "pdf2word" | "pdftoword":
            if files:
                pdf_to_word(files[0])
        case "word2pdf" | "wordtopdf":
            if files:
                word_to_pdf(files[0])
        case "img2pdf" | "imagetopdf":
            if files:
                images_to_pdf(files)
        case "pdf2img" | "pdf2jpg":
            if files:
                pdf_to_images(files[0])
        case "html2pdf":
            if files:
                html_to_pdf(files[0])
        case "vidtomp3" | "vid2mp3" | "video2mp3" | "videotomp3":
            if files:
                video_to_mp3(files[0])
        case _:
            print(f"❌ Unknown or incomplete convert command: {' '.join(args)}")
            show_help()
