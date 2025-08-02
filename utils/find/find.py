import sys
import os
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

def search_in_directory(directory, target_name, deep=False):
    """Search files in a single directory."""
    matches = []
    try:
        for entry in os.scandir(directory):
            if entry.name.lower() == target_name.lower():
                matches.append(Path(entry.path).resolve())
            if deep and entry.is_dir(follow_symlinks=False):
                matches.extend(search_in_directory(entry.path, target_name, deep))
    except (PermissionError, FileNotFoundError):
        pass
    return matches

def find_file(name, deep=False):
    """Main finder with controlled parallelism."""
    start_dir = Path.cwd()
    targets = [p for p in start_dir.iterdir() if p.is_dir()] if deep else [start_dir]

    matches = []
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(search_in_directory, d, name, deep): d for d in targets}
        for future in as_completed(futures):
            matches.extend(future.result())

    if not deep:
        matches.extend(search_in_directory(start_dir, name, deep))

    return matches

def main(args=None):
    if args is None or not args:
        print("Usage: faiz find <filename> [--deep]")
        return

    name = args[0]
    deep = '--deep' in args

    print(f"🔍 Searching for '{name}'{' deeply' if deep else ''}...\n")
    start_time = time.time()

    results = find_file(name, deep)

    elapsed = time.time() - start_time
    
    if results:
        print(f"✅ Found {len(results)} result(s) in {elapsed:.2f} seconds:\n")
        for path in results:
            print(f"👉 file:///{path}")
    else:
        print(f"❌ No matches found (searched in {elapsed:.2f} seconds).")
