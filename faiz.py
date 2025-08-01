
import sys
from .utils.env.env import main as env_main
from .utils.edge.edge import edge_main_func, edgeMobileFun
from .utils.git import main as git_main
from .utils.qr import main as qr
from .utils.cursor import main as cursor_main
from .utils.count.count import main as count_files_command
from .utils.ssh.ssh import main as ssh_command
from .utils.framework.react import main as setup_reactjs
from .utils.framework.laravel import main as setup_laravel
from .utils.search.search import main as google_search
from .utils.find.find import main as find_main
from .utils.folder.folder import main as folder_main
# This is all converter imports
from .utils.converter.webp.webpcon import main as webp_con
from .utils.converter.avif.avifcon import main as avif_main
from .utils.converter.jpeg.jpegcon import main as jpeg_main
from .utils.converter.png.pngcon import main as png_main

from .utils.convert.convert import main as convert_main
# from .utils.hacker.hacker import main as hacker_main
from .utils.pdf.pdf import main as pdf_main
from .utils.zip.zip import main as zip_main
VERSION = "0.1.6"

commands = {
    "avif": avif_main,
    "ssh": ssh_command,
    "reactjs": setup_reactjs,
    "laravel": setup_laravel,
    "search": google_search,
    "edge": lambda args: edge_main_func(args),
    "edge_mobile": lambda args: edgeMobileFun(args),
    "webp": webp_con,
    "git": git_main,
    "qr": qr,
    "cursor": cursor_main,
    "count": count_files_command,
    "env": env_main,
    "--version": lambda args: print(f"🛠️  Faiz Super Command: {VERSION}"),
    "png": png_main,
    "jpeg": jpeg_main,
    "pdf":pdf_main,
    "convert":convert_main,
    "zip":zip_main,
    "find":find_main,
    "folder":folder_main,
    "open":folder_main,
    
}


def list_commands():
    print("\n📜 Available Commands:")
    print("=" * 25)
    for cmd in sorted(commands.keys()):
        print(f"👉 {cmd}")
    print("\nExample: faiz webp *.jpg")
    print("=" * 25)


def invalid_command(args):
    print('invalid command')


def main():
    if len(sys.argv) < 2:
        list_commands()
        sys.exit(1)

    command = sys.argv[1].lower()
    args = sys.argv[2:]

    func = commands.get(command, invalid_command)
    func(args)


if __name__ == "__main__":
    main()
