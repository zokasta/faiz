import json
import os
import subprocess
import sys

PROFILE_FILE = "ssh_profiles.json"
RESERVED_NAMES = {"create", "update", "delete", "remove", "list", "help"}


def load_profiles():
    if not os.path.exists(PROFILE_FILE):
        return {}
    with open(PROFILE_FILE, "r") as f:
        return json.load(f)


def save_profiles(profiles):
    with open(PROFILE_FILE, "w") as f:
        json.dump(profiles, f, indent=4)


def list_profiles(profiles):
    if not profiles:
        print("❌ No SSH profiles found.")
        return
    print("🔑 Saved SSH Profiles:")
    for name, details in profiles.items():
        print(f" - {name}: {details}")


def create_profile(profiles):
    name = input("Enter profile name: ").strip().lower()
    if not name:
        print("❌ Profile name cannot be empty.")
        return
    if name in profiles:
        print("❌ Profile already exists.")
        return
    if name in RESERVED_NAMES:
        print(f"❌ '{name}' is a reserved word and cannot be used as a profile name.")
        return

    ssh_command = input("Enter SSH command (e.g., ssh user@host or full command with options): ").strip()
    if not ssh_command:
        print("❌ SSH command cannot be empty.")
        return

    profiles[name] = ssh_command
    save_profiles(profiles)
    print(f"✅ Profile '{name}' created successfully.")


def delete_profile(profiles, name):
    name = name.lower()
    if name not in profiles:
        print(f"❌ Profile '{name}' not found.")
        return
    del profiles[name]
    save_profiles(profiles)
    print(f"🗑️ Profile '{name}' deleted.")


def update_profile(profiles, name):
    name = name.lower()
    if name not in profiles:
        print(f"❌ Profile '{name}' not found.")
        return
    print(f"Current command: {profiles[name]}")
    new_command = input("Enter new SSH command: ").strip()
    if not new_command:
        print("❌ SSH command cannot be empty.")
        return
    profiles[name] = new_command
    save_profiles(profiles)
    print(f"🔄 Profile '{name}' updated.")


def connect_to_profile(profiles, name):
    name = name.lower()
    if name not in profiles:
        print(f"❌ Profile '{name}' not found.")
        return
    command = profiles[name]
    print(f"🚀 Connecting using: {name}")
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"❌ Failed to connect: {e}")


def main(args):
    profiles = load_profiles()

    if not args or args[0].lower() in {"help", "--help", "-h"}:
        print("""
Usage:
  faiz ssh list                          List all saved SSH profiles
  faiz ssh create                        Create a new SSH profile
  faiz ssh delete <name>                 Delete a saved SSH profile
  faiz ssh update <name>                 Update an existing SSH profile
  faiz ssh <name>                        Connect to a saved SSH profile
""")
        return

    command = args[0].lower()

    if command == "list":
        list_profiles(profiles)
    elif command == "create":
        create_profile(profiles)
    elif command == "delete":
        if len(args) < 2:
            print("❌ Please provide the profile name to delete.")
            return
        delete_profile(profiles, args[1])
    elif command == "update":
        if len(args) < 2:
            print("❌ Please provide the profile name to update.")
            return
        update_profile(profiles, args[1])
    else:
        if command in RESERVED_NAMES:
            print(f"❌ '{command}' is a reserved word and cannot be used as a profile name.")
            return
        connect_to_profile(profiles, command)


