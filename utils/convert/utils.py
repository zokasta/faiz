from pathlib import Path
import getpass
import os


def prompt_password():
    try:
        return getpass.getpass("\U0001F511 Enter PDF password: ")
    except Exception as e:
        print(f"❌ Error reading password: {e}")
        return None


def get_output_path(input_file, filename):
    input_path = Path(input_file)
    is_absolute = input_path.is_absolute()
    downloads_dir = Path.home() / "Downloads"
    if is_absolute:
        return str(downloads_dir / filename)
    return str(Path.cwd() / filename)

