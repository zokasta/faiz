from pathlib import Path
import logging
import pikepdf
from .utils import prompt_password, get_output_path  # ✅ Import helper

# ✅ Suppress pikepdf INFO logs
logging.getLogger("pikepdf").propagate = False
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
        pdf = pikepdf.open(file)
        out_name = f"locked_{Path(file).name}"
        out_path = get_output_path(file, out_name)  # ✅ Use helper
        pdf.save(out_path, encryption=pikepdf.Encryption(owner=pwd, user=pwd, R=4))
        print(f"🔒 Locked PDF saved as: {out_path}")
    except Exception as e:
        print(f"❌ Lock failed: {e}")
