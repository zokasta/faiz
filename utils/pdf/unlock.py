from pathlib import Path
import logging
import pikepdf
from .utils import prompt_password, get_output_path  # ✅ Import get_output_path

# ✅ Suppress pikepdf INFO logs
logging.getLogger("pikepdf").propagate = False

def unlock_pdf(file_path, password=None):
    "🔓 Unlock a password-protected PDF."
    if not Path(file_path).is_file():
        print("❌ File not found.")
        return

    password = password or prompt_password()
    try:
        pdf = pikepdf.open(file_path, password=password)
        out_name = f"unlocked_{Path(file_path).name}"
        out_path = get_output_path(file_path, out_name)  # ✅ Determine correct output path
        pdf.save(out_path)
        print(f"🔓 Unlocked PDF saved as: {out_path}")
    except pikepdf._qpdf.PasswordError:
        print("❌ Incorrect password.")
    except Exception as e:
        print(f"❌ Unlock failed: {e}")
