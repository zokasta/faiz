from pathlib import Path
import zipfile
from ..pdf.utils import get_output_path

def main(args):
    """
    📦 Zip files or folders into a single archive.
    Usage: faiz zip <file_or_folder> [more files...] [--output name.zip]
    """
    if not args:
        print("❗ Usage: zip <file_or_folder> [more files...] [--output name.zip]")
        return

    # Handle optional --output flag
    if '--output' in args:
        index = args.index('--output')
        output_name = args[index + 1] if index + 1 < len(args) else "archive.zip"
        items = args[:index]
    else:
        output_name = "archive.zip"
        items = args

    if not items:
        print("❗ No files or folders specified.")
        return

    try:
        out_path = get_output_path(items[0], output_name)
        with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for item in items:
                path = Path(item)
                if not path.exists():
                    print(f"⚠️ Skipped (not found): {item}")
                    continue
                if path.is_dir():
                    for file in path.rglob("*"):
                        if file.is_file():
                            zipf.write(file, file.relative_to(path.parent))
                else:
                    zipf.write(path, path.name)
        print(f"✅ Zipped into: {out_path}")
    except Exception as e:
        print(f"❌ Zipping failed: {e}")
