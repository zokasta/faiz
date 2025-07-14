from pathlib import Path
from .utils import prompt_password, get_output_path

# Suppress pikepdf/qpdf stderr messages
import sys
import os
import contextlib

@contextlib.contextmanager
def suppress_stderr():
    with open(os.devnull, 'w') as devnull:
        old_stderr = sys.stderr
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stderr = old_stderr

with suppress_stderr():
    import pikepdf

def main(args):
    if not args:
        print("❗ Usage: lock <file.pdf> [--password pwd]")
        return

    file = args[0]
    pwd = args[args.index('--password')+1] if '--password' in args else prompt_password()

    if not Path(file).exists():
        print("❌ File not found.")
        return

    try:
        with suppress_stderr():
            pdf = pikepdf.open(file)

        out_name = f"locked_{Path(file).name}"
        out_path = get_output_path(file, out_name)

        pdf.save(out_path, encryption=pikepdf.Encryption(owner=pwd, user=pwd, R=4))
        print(f"🔒 Locked PDF saved as: {out_path}")
    except Exception as e:
        print(f"❌ Lock failed: {e}")
