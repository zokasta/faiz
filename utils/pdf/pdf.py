"""
Faiz PDF Suite - Master PDF Toolkit
All tools integrated into one module.
"""

import os
import sys
import getpass
import signal
from pathlib import Path

import pikepdf
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

# Safe exit on interrupts
if True:
    def handle_exit(signum, frame):
        print("\n🚪 Exiting Faiz PDF Suite. Goodbye!")
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

# Helper: prompt for password
if True:
    def prompt_password():
        try:
            return getpass.getpass("🔑 Enter PDF password: ")
        except Exception as e:
            print(f"❌ Error reading password: {e}")
            sys.exit(1)

# === Command Implementations ===

def lock_pdf(file_path, password=None):
    "🔒 Lock a PDF with a password."
    if not Path(file_path).is_file():
        print("❌ File not found.")
        return
    password = password or prompt_password()
    try:
        pdf = pikepdf.open(file_path)
        out = f"locked_{Path(file_path).name}"
        pdf.save(out, encryption=pikepdf.Encryption(owner=password, user=password, R=4))
        print(f"🔒 Locked PDF saved as: {out}")
    except Exception as e:
        print(f"❌ Lock failed: {e}")


def unlock_pdf(file_path, password=None):
    "🔓 Unlock a password-protected PDF."
    if not Path(file_path).is_file():
        print("❌ File not found.")
        return
    password = password or prompt_password()
    try:
        pdf = pikepdf.open(file_path, password=password)
        out = f"unlocked_{Path(file_path).name}"
        pdf.save(out)
        print(f"🔓 Unlocked PDF saved as: {out}")
    except pikepdf._qpdf.PasswordError:
        print("❌ Incorrect password.")
    except Exception as e:
        print(f"❌ Unlock failed: {e}")


def merge_pdfs(inputs, output):
    "📄 Merge multiple PDFs into one."
    merger = PdfMerger()
    try:
        for f in inputs:
            if Path(f).is_file():
                merger.append(f)
            else:
                print(f"⚠️ Skipped (not found): {f}")
        merger.write(output)
        merger.close()
        print(f"✅ PDFs merged into: {output}")
    except Exception as e:
        print(f"❌ Merge failed: {e}")


def split_pdf(file_path):
    "✂️ Split a PDF into individual pages."
    if not Path(file_path).is_file():
        print("❌ File not found.")
        return
    try:
        reader = PdfReader(file_path)
        for i, page in enumerate(reader.pages, 1):
            writer = PdfWriter()
            writer.add_page(page)
            out = f"{Path(file_path).stem}_page_{i}.pdf"
            with open(out, 'wb') as f:
                writer.write(f)
            print(f"📄 Page {i} saved as: {out}")
    except Exception as e:
        print(f"❌ Split failed: {e}")

# Stubs for future features
# def compress_pdf(...)
# def rotate_pdf(...)
# def add_page_numbers(...)
# etc.

# === Dispatcher ===

def main(args):
    if not args:
        print("""
📚 Faiz PDF Suite - Usage Guide 🔧

Usage:
  👉 faiz pdf lock <file.pdf> [--password <pwd>]     🔒 Lock a PDF
  👉 faiz pdf unlock <file.pdf> [--password <pwd>]   🔓 Unlock a PDF
  👉 faiz pdf merge <in1.pdf> <in2.pdf> ... <out.pdf> 📄 Merge PDFs
  👉 faiz pdf split <file.pdf>                       ✂️ Split into pages

Options:
  --password <pwd>    Provide password inline
  --help              Show this help message

Examples:
  faiz pdf lock report.pdf
  faiz pdf unlock locked_report.pdf --password 1234
  faiz pdf merge a.pdf b.pdf merged.pdf
  faiz pdf split document.pdf
""")
        return

    cmd = args[0].lower()

    if cmd == 'lock':
        file = args[1] if len(args) > 1 else None
        pwd = args[args.index('--password')+1] if '--password' in args else None
        if not file:
            print("❗ Missing file to lock.")
            return
        lock_pdf(file, pwd)

    elif cmd == 'unlock':
        file = args[1] if len(args) > 1 else None
        pwd = args[args.index('--password')+1] if '--password' in args else None
        if not file:
            print("❗ Missing file to unlock.")
            return
        unlock_pdf(file, pwd)

    elif cmd == 'merge':
        if len(args) < 4:
            print("❗ Provide at least two input PDFs and an output filename.")
            return
        merge_pdfs(args[1:-1], args[-1])

    elif cmd == 'split':
        file = args[1] if len(args) > 1 else None
        if not file:
            print("❗ Missing file to split.")
            return
        split_pdf(file)

    else:
        print(f"❌ Unknown command: {cmd}")
        print("Run 'faiz pdf' for usage details.")

if __name__ == '__main__':
    main(sys.argv[1:])
