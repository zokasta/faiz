import os
import json
import sys
from pathlib import Path

CONFIG_FILE = Path.home() / ".faiz_folder.json"

def save_folder_path(folder_path):
    """Save selected folder path to config file."""
    with open(CONFIG_FILE, "w") as f:
        json.dump({"folder": str(folder_path)}, f)

def load_folder_path():
    """Load previously saved folder path."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r") as f:
            return Path(json.load(f).get("folder", ""))
    return None

def make_file(filetype, filename):
    """Create different types of files in the selected folder."""
    folder = load_folder_path()
    if not folder or not folder.exists():
        print("❌ No folder set. Run: faiz folder")
        return

    filepath = folder / filename

    if filetype == "word":
        filepath = filepath.with_suffix(".docx")
    elif filetype == "ppt":
        filepath = filepath.with_suffix(".pptx")
    elif filetype == "excel":
        filepath = filepath.with_suffix(".xlsx")
    elif filetype == "text":
        filepath = filepath.with_suffix(".txt")
    elif filetype == "doc":
        filepath = filepath.with_suffix(".url")
        filepath.write_text("[InternetShortcut]\nURL=https://docs.google.com/document/create")
        print(f"🌐 Google Docs shortcut created: {filepath}")
        return
    elif filetype == "sheet":
        filepath = filepath.with_suffix(".url")
        filepath.write_text("[InternetShortcut]\nURL=https://docs.google.com/spreadsheets/create")
        print(f"🌐 Google Sheets shortcut created: {filepath}")
        return
    elif filetype == "slide":
        filepath = filepath.with_suffix(".url")
        filepath.write_text("[InternetShortcut]\nURL=https://docs.google.com/presentation/create")
        print(f"🌐 Google Slides shortcut created: {filepath}")
        return

    filepath.touch()
    print(f"✅ Created {filetype} file: {filepath}")

def open_file(filename=None):
    """Open folder or a specific file."""
    folder = load_folder_path()
    if not folder or not folder.exists():
        print("❌ No folder set. Run: faiz folder")
        return

    if not filename:
        os.startfile(folder)
        print(f"📂 Opened folder: {folder}")
    else:
        matches = [f for f in folder.iterdir() if filename.lower() in f.name.lower()]
        if matches:
            os.startfile(matches[0])
            print(f"📄 Opened file: {matches[0]}")
        else:
            print(f"❌ No file matching '{filename}' found in {folder}")

def list_files():
    """List all files and folders in the selected directory."""
    folder = load_folder_path()
    if not folder or not folder.exists():
        print("❌ No folder set. Run: faiz folder")
        return

    items = list(folder.iterdir())
    if not items:
        print(f"📂 {folder} is empty.")
    else:
        print(f"\n📜 Contents of {folder}:\n" + "="*40)
        for item in items:
            item_type = "[DIR]" if item.is_dir() else "[FILE]"
            print(f"{item_type} {item.name}")
        print("="*40)

def set_folder():
    """Prompt user to set or update folder path."""
    folder_path = input("📂 Drag and drop folder or enter path: ").strip().strip('"')
    folder = Path(folder_path)
    if folder.exists() and folder.is_dir():
        save_folder_path(folder)
        print(f"✅ Folder set to: {folder}")
    else:
        print("❌ Invalid folder path.")

def main(args):
    if not args:
        # If no arguments, show current folder or ask to set
        current = load_folder_path()
        if current and current.exists():
            print(f"📂 Current folder: {current}")
        else:
            print("❌ No folder set.")
            set_folder()
        return

    if args[0] == "update:path":
        set_folder()
    elif args[0] == "list":
        list_files()
    elif args[0].startswith("make:"):
        filetype = args[0].split(":")[1]
        filename = args[1] if len(args) > 1 else "untitled"
        make_file(filetype, filename)
    elif args[0] == "open":
        filename = args[1] if len(args) > 1 else None
        open_file(filename)
    else:
        print("❌ Invalid folder command.")
