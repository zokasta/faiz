import sys
import signal
from . import lock, unlock, merge, split, compress, rotate, pagenum, repair, corrupt

def handle_exit(signum, frame):
    print("\n🚪 Exiting Faiz PDF Suite. Goodbye!")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not args:
        print("""
📚 Faiz PDF Suite - Usage Guide 🔧

Usage:
  faiz pdf <command> [options]

Commands:
  🔒 lock <file.pdf> [--password pwd]
  🔓 unlock <file.pdf> [--password pwd]
  📄 merge <in1.pdf> <in2.pdf> ... <out.pdf>
  ✂️ split <file.pdf>
  📦 compress <file.pdf> [--output name]
  🔃 rotate <file.pdf> <angle> [--output name]
  🔢 pagenum <file.pdf> [--output name]
  🛠️ repair <file.pdf>
  💥 corrupt <file.pdf> [--impossible]

Examples:
  faiz pdf lock secret.pdf
  faiz pdf unlock secret.pdf --password 1234
  faiz pdf merge a.pdf b.pdf output.pdf
  faiz pdf compress large.pdf
  faiz pdf corrupt file.pdf --impossible
""")
        return

    cmd = args[0].lower()
    opts = args[1:]

    match cmd:
        case 'lock': lock.main(opts)
        case 'unlock': unlock.main(opts)
        case 'merge': merge.main(opts)
        case 'split': split.main(opts)
        case 'compress': compress.main(opts)
        case 'rotate': rotate.main(opts)
        case 'pagenum': pagenum.main(opts)
        case 'repair': repair.main(opts)
        case 'corrupt':
            impossible = '--impossible' in opts
            file = next((f for f in opts if not f.startswith('--')), None)
            if file:
                corrupt.corrupt_pdf(file, impossible=impossible)
            else:
                print("❗ Usage: corrupt <file.pdf> [--impossible]")
        case _: print(f"❌ Unknown command: {cmd}\nRun `faiz pdf` for help.")
