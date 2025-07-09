import os
import glob

def main(args):
    if not args or args[0] not in {"*", "type"}:
        print("Usage:\n  faiz count * [--index]\n  faiz count type <pattern>")
        return

    show_index = "--index" in args

    if args[0] == "*":
        categories = {
            "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".avif"},
            "Audio": {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"},
            "Video": {".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv"},
            "Documents": {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".md"},
        }

        counts = {name: 0 for name in categories}
        counts["Other Files"] = 0
        folder_count = 0

        indexed_list = []

        for idx, entry in enumerate(os.scandir(), start=1):
            name = entry.name
            if entry.is_dir():
                folder_count += 1
                if show_index:
                    indexed_list.append(f"{idx}. 📁 {name}/")
            elif entry.is_file():
                ext = os.path.splitext(name.lower())[1]
                for cat, exts in categories.items():
                    if ext in exts:
                        counts[cat] += 1
                        break
                else:
                    counts["Other Files"] += 1

                if show_index:
                    indexed_list.append(f"{idx}. 📄 {name}")

        print(f"📁 Folders: {folder_count}")
        for cat, num in counts.items():
            print(f"📄 {cat}: {num}")

        total_items = folder_count + sum(counts.values())
        print(f"\n🔢 Total entries (files + folders): {total_items}")

        if show_index and indexed_list:
            print("\n📝 Index of Files and Folders:")
            print("-" * 30)
            for line in indexed_list:
                print(line)

    elif args[0] == "type" and len(args) > 1:
        pattern = args[1]
        matching = glob.glob(pattern)
        file_count = sum(1 for p in matching if os.path.isfile(p))
        folder_count = sum(1 for p in matching if os.path.isdir(p))
        print(f"📂 Total matching entries for '{pattern}': {len(matching)}")
        print(f"   - Files:   {file_count}")
        print(f"   - Folders: {folder_count}")
    else:
        print("❌ Invalid usage.\nUse:\n  faiz count * [--index]\n  faiz count type <pattern>")
