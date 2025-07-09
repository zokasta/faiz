import os
import sys
import subprocess
import glob
import requests
import webbrowser
from .utils.env.env import main as env_main
from bs4 import BeautifulSoup
from .utils.edge.edge import edge_main_func, edgeMobileFun
from .utils.webp.webpcon import convert_to_webp, process_images
from .utils.avif.avifcon import main as avif_main
from .utils.git import main as git_main
from .utils.qr import main as qr
from .utils.cursor import main as cursor_main
from .utils.count.count import main as count_files_command
from .utils.ssh.ssh import main as ssh_command
from .utils.framework.react import main as setup_reactjs
from .utils.framework.laravel import main as setup_laravel
from .utils.search.search import main as google_search
from .utils.webp.webpcon import main as webp_con


VERSION = "0.1.1"

commands = {
    "avif": avif_main,
    "ssh": ssh_command,
    "reactjs": setup_reactjs,
    "laravel": setup_laravel,
    "search": google_search,
    "edge": lambda args: edge_main_func(20),
    "edge_mobile": lambda args: edgeMobileFun(20),
    "webp": webp_con,
    "git": git_main,
    "qr": qr,
    "cursor": cursor_main,
    "count": count_files_command,
    "env": env_main,
    "version": lambda args: print(f"🛠️  Faiz Super Command Version: {VERSION}"),
    "--version": lambda args: print(f"🛠️  Faiz Super Command: {VERSION}"),
    "list": lambda args: list_commands()
}


def list_commands():
    print("\n📜 Available Commands:")
    print("=" * 25)
    for cmd in sorted(commands.keys()):
        print(f"👉 {cmd}")
    print("\nExample: faiz webp *.jpg")
    print("=" * 25)


def invalid_command(args):
    print("❌ Invalid subcommand.")
    print("👉 Run `faiz list` to see all available commands.")


def main():
    if len(sys.argv) < 2:
        print("⚠️  No subcommand provided.")
        print("👉 Run `faiz list` to see available commands.")
        sys.exit(1)

    command = sys.argv[1].lower()
    args = sys.argv[2:]

    func = commands.get(command, invalid_command)
    func(args)


if __name__ == "__main__":
    main()
