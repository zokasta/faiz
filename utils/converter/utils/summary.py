import time

def format_size(bytes_size):
    return f"{bytes_size / (1024 * 1024):.2f} MB" if bytes_size >= 1024 * 1024 else f"{bytes_size / 1024:.2f} KB"

def print_summary(stats):
    duration = time.time() - stats["start_time"]
    total_in = stats["total_input_size"]
    total_out = stats["total_output_size"]
    total_saved = total_in - total_out
    avg_in = total_in / stats["converted"] if stats["converted"] else 0
    avg_out = total_out / stats["converted"] if stats["converted"] else 0
    avg_reduction = 100 * (avg_in - avg_out) / avg_in if avg_in else 0

    print("\n📊 Conversion Summary")
    print("===========================")
    print(f"🖼️  Total Images:         {stats['total_images']}")
    print(f"✅ Successfully Converted: {stats['converted']}")
    print(f"⏩ Skipped:               {stats['skipped']}")
    print(f"❌ Failed:                {stats['failed']}")
    print(f"⏱️  Total Time:           {duration:.2f} seconds")
    if stats["converted"]:
        print(f"\n📦 Size Summary:")
        print(f"📥 Total Before:         {format_size(total_in)}")
        print(f"📤 Total After:          {format_size(total_out)}")
        print(f"📉 Total Saved:          {format_size(total_saved)}")
        print(f"⚖️  Avg Before:           {format_size(avg_in)}")
        print(f"⚖️  Avg After:            {format_size(avg_out)}")
        print(f"🔻 Avg Reduction:         {avg_reduction:.2f}%")
    print("===========================\n")
