import os
import glob
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def human_readable_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"

def process_file(path, categories):
    name = os.path.basename(path)
    ext = os.path.splitext(name.lower())[1]
    try:
        size = os.path.getsize(path)
    except:
        size = 0  # Handle unreadable files safely

    for cat, exts in categories.items():
        if ext in exts:
            return (cat, size, name)
    return ("Other Files", size, name)

def show_progress(progress, stop_event):
    while not stop_event.is_set():
        print(f"\r🔄 Files processed: {progress['count']} | Total size: {human_readable_size(progress['size'])}", end='', flush=True)
        time.sleep(1)
    print(f"\r✅ Files processed: {progress['count']} | Total size: {human_readable_size(progress['size'])}")

def main(args):
    if not args:
        print("Usage:\n  faiz count * [--index] [--deep]\n  faiz count <pattern>\n  faiz count folder")
        return

    show_index = "--index" in args
    deep_search = "--deep" in args

    filtered_args = [arg for arg in args if arg not in {"--index", "--deep"}]
    if not filtered_args:
        print("❌ Missing arguments.\nUsage:\n  faiz count * [--index] [--deep]\n  faiz count <pattern>\n  faiz count folder")
        return

    command = filtered_args[0]

    categories = {
        "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".avif"},
        "Audio": {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"},
        "Video": {".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv"},
        "Documents": {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".md"},
    }

    if command == "folder":
        search_path = "**" if deep_search else "."
        folder_count = sum(1 for root, dirs, files in os.walk(search_path) for d in dirs)
        print(f"📁 Total folders{' (deep search)' if deep_search else ''}: {folder_count}")
        return

    if command == "*":
        counts = {name: 0 for name in categories}
        sizes = {name: 0 for name in categories}
        counts["Other Files"] = 0
        sizes["Other Files"] = 0
        folder_count = 0
        indexed_list = []

        entries = []
        if deep_search:
            for root, dirs, files in os.walk("."):
                for d in dirs:
                    entries.append(os.path.join(root, d))
                for f in files:
                    entries.append(os.path.join(root, f))
        else:
            entries = [entry.path for entry in os.scandir()]

        files = [e for e in entries if os.path.isfile(e)]
        folders = [e for e in entries if os.path.isdir(e)]
        folder_count = len(folders)

        progress = {"count": 0, "size": 0}
        stop_event = threading.Event()

        with ThreadPoolExecutor() as executor:
            if deep_search:
                progress_thread = threading.Thread(target=show_progress, args=(progress, stop_event))
                progress_thread.start()

            futures = {executor.submit(process_file, path, categories): path for path in files}
            for idx, future in enumerate(as_completed(futures), start=1):
                try:
                    cat, size, name = future.result()
                    counts[cat] += 1
                    sizes[cat] += size
                    progress["count"] += 1
                    progress["size"] += size
                    if show_index:
                        indexed_list.append(f"{idx}. 📄 {name} — {human_readable_size(size)}")
                except:
                    continue

            if deep_search:
                stop_event.set()
                progress_thread.join()

        print(f"\n📁 Folders: {folder_count}")
        total_size = sum(sizes.values())
        for cat, num in counts.items():
            size = sizes[cat]
            print(f"📄 {cat}: {num} files — {human_readable_size(size)}")

        total_items = folder_count + sum(counts.values())
        print(f"\n🔢 Total entries: {total_items}")
        print(f"💾 Total size: {human_readable_size(total_size)}")

        if show_index and indexed_list:
            print("\n📝 Index:")
            print("-" * 30)
            for line in indexed_list:
                print(line)
        return

    # Handle pattern search
    pattern = command
    search_pattern = f"**/{pattern}" if deep_search else pattern
    matching = glob.glob(search_pattern, recursive=deep_search)

    files = [p for p in matching if os.path.isfile(p)]
    folders = [p for p in matching if os.path.isdir(p)]

    total_size = 0
    progress = {"count": 0, "size": 0}
    stop_event = threading.Event()

    with ThreadPoolExecutor() as executor:
        if deep_search:
            progress_thread = threading.Thread(target=show_progress, args=(progress, stop_event))
            progress_thread.start()

        futures = {executor.submit(os.path.getsize, f): f for f in files}
        for future in as_completed(futures):
            try:
                size = future.result()
                total_size += size
                progress["count"] += 1
                progress["size"] += size
            except:
                continue

        if deep_search:
            stop_event.set()
            progress_thread.join()

    print(f"\n📂 Total matching entries for '{pattern}'{' (deep search)' if deep_search else ''}: {len(matching)}")
    print(f"   - Files:   {len(files)}")
    print(f"   - Folders: {len(folders)}")
    print(f"💾 Total size of matching files: {human_readable_size(total_size)}")

