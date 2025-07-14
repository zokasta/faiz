from pathlib import Path
from .utils import prompt_password, get_output_path

# --- Suppress C++ logging from pikepdf/qpdf ---
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

# Suppress during pikepdf import/init
with suppress_stderr():
    import pikepdf

def unlock_pdf(file_path, password=None):
    "🔓 Unlock a password-protected PDF."
    if not Path(file_path).is_file():
        print("❌ File not found.")
        return

    password = password or prompt_password()
    try:
        with suppress_stderr():  # Also suppress on open (just in case)
            pdf = pikepdf.open(file_path, password=password)

        out_name = f"unlocked_{Path(file_path).name}"
        out_path = get_output_path(file_path, out_name)
        pdf.save(out_path)
        print(f"🔓 Unlocked PDF saved as: {out_path}")
    except pikepdf._qpdf.PasswordError:
        print("❌ Incorrect password.")
    except Exception as e:
        print(f"❌ Unlock failed: {e}")
