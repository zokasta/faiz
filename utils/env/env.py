import json
import os

# Store the env.json in a fixed location:
ENV_DIR = os.path.join(os.path.expanduser("~"), ".faiz")
ENV_FILE = os.path.join(ENV_DIR, "env.json")

# Load or create env.json safely
def load_env():
    if not os.path.exists(ENV_DIR):
        os.makedirs(ENV_DIR)

    if not os.path.exists(ENV_FILE):
        with open(ENV_FILE, 'w') as f:
            json.dump({}, f, indent=4)

    with open(ENV_FILE, 'r') as f:
        return json.load(f)

# Save env.json
def save_env(env_data):
    with open(ENV_FILE, 'w') as f:
        json.dump(env_data, f, indent=4)

# Get value (NO PRINT)
def get_env(key):
    env = load_env()
    return env.get(key)

# List all
def list_env():
    env = load_env()
    if not env:
        print("⚠️ No variables set.")
    else:
        for k, v in env.items():
            print(f"{k} = {v}")

# Add or update
def add_env(key, value):
    env = load_env()
    env[key] = value
    save_env(env)
    print(f"✅ {key} added/updated.")

# Remove key
def remove_env(key):
    env = load_env()
    if key in env:
        del env[key]
        save_env(env)
        print(f"✅ {key} removed.")
    else:
        print(f"❌ {key} not found.")

# Command Line Handler
def main(args):
    if not args:
        print('''
Usage:
  faiz env get KEY
  faiz env list
  faiz env add KEY VALUE
  faiz env remove KEY
''')
        return

    cmd = args[0]

    if cmd == 'get' and len(args) >= 2:
        value = get_env(args[1])
        if value is None:
            print(f"❌ {args[1]} not found.")
        else:
            print(f"{args[1]} = {value}")

    elif cmd == 'list':
        list_env()

    elif cmd == 'add' and len(args) >= 3:
        key = args[1]
        value = args[2]
        add_env(key, value)

    elif cmd == 'remove' and len(args) >= 2:
        remove_env(args[1])

    else:
        print("❌ Invalid command or missing arguments.")
