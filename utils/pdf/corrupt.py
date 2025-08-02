from pathlib import Path
from .utils import get_output_path

def corrupt_pdf(file_path, impossible=False):
    "⚠️ Corrupt a PDF — safely or irreparably based on mode."

    if not Path(file_path).is_file():
        print("❌ File not found.")
        return

    try:
        with open(file_path, "rb") as original:
            content = bytearray(original.read())

        if impossible:
            # Brutally destroy key structure - PDF header + xref + trailer
            for i in range(0, min(1024, len(content))):
                content[i] = 0x00  # overwrite with nulls
            name = f"impossible_{Path(file_path).name}"
        else:
            # Safe corruption: flip some middle bytes randomly
            corrupt_range = range(500, min(1500, len(content)))
            for i in corrupt_range:
                if i % 2 == 0:
                    content[i] = (content[i] ^ 0xAA)  # XOR corruption
            name = f"corrupted_{Path(file_path).name}"

        out_path = get_output_path(file_path, name)
        with open(out_path, "wb") as f:
            f.write(content)

        status = "💥 Impossible to repair" if impossible else "🩹 Safely corrupted"
        print(f"{status}: {out_path}")

    except Exception as e:
        print(f"❌ Failed to corrupt file: {e}")
