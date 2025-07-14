from pathlib import Path
import getpass
import sys
import signal

# Safe exit
def handle_exit(signum, frame):
    print("\n🚪 Exiting Faiz PDF Suite. Goodbye!")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

# Prompt for password
def prompt_password():
    try:
        return getpass.getpass("🔑 Enter PDF password: ")
    except Exception as e:
        print(f"❌ Error reading password: {e}")
        sys.exit(1)
    

def get_output_path(input_path, filename):
    """
    Determine where to save the output:
    - If input_path is absolute → save to Downloads folder.
    - If input_path is relative → save to current directory.
    """
    folder = (Path.home() / "Downloads") if Path(input_path).is_absolute() else Path.cwd()
    return folder / filename
