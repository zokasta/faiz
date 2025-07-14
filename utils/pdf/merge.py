from pathlib import Path
from PyPDF2 import PdfMerger
from .utils import get_output_path  # ✅ Import the helper

def merge_pdfs(inputs, output_name):
    "📄 Merge multiple PDFs into one."
    merger = PdfMerger()
    try:
        for f in inputs:
            if Path(f).is_file():
                merger.append(f)
            else:
                print(f"⚠️ Skipped (not found): {f}")

        # Use first valid input file to decide output folder
        base_input = next((f for f in inputs if Path(f).is_file()), None)
        if base_input is None:
            print("❌ No valid input files found.")
            return

        out_path = get_output_path(base_input, output_name)  # ✅ Use helper
        merger.write(out_path)
        merger.close()
        print(f"✅ PDFs merged into: {out_path}")
    except Exception as e:
        print(f"❌ Merge failed: {e}")
