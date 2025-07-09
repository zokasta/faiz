import os
import sys
import subprocess
import requests
import json
from .env.env import get_env

# Set your base projects directory
BASE_PATH = "Z:/Projects"
CLONE_PATH = os.path.join(BASE_PATH, "clone")  # Store cloned repos inside /clone
PROJECTS_JSON = os.path.join(BASE_PATH, "projects.json")

# GitHub credentials (read from environment variables for security)


GITHUB_TOKEN = get_env('GITHUB_TOKEN')
GITHUB_USERNAME = get_env('GITHUB_USERNAME')


def main(args):
    if len(sys.argv) < 3:
        print("Usage: python script.py git <make|run|clone|list> <folder_name> [repo_url]")
        return

    command = sys.argv[1]  # 'git'
    action = sys.argv[2]   # 'make', 'run', 'clone', or 'list'

    # For make, run, and clone commands we require folder_name (and clone also requires repo_url)
    folder_name = sys.argv[3] if len(sys.argv) > 3 else None
    repo_url = sys.argv[4] if len(sys.argv) > 4 else None

    if command == "git":
        if action == "make":
            create_project(folder_name)
        elif action == "run":
            open_project(folder_name)
        elif action == "clone":
            if not repo_url:
                print("❌ Please provide a GitHub repository URL.")
                return
            clone_project(repo_url, folder_name)
        elif action == "list":
            list_projects()
        else:
            print("Invalid action. Use 'make', 'run', 'clone', or 'list'.")

def create_project(folder_name):
    if not folder_name:
        print("❌ Please provide a folder name.")
        return

    folder_path = os.path.join(BASE_PATH, folder_name)
    use_git = input("Do you want to use GitHub for this project? (yes/no): ").strip().lower() == "yes"

    try:
        os.makedirs(folder_path, exist_ok=True)
        print(f"📂 Folder created: {folder_path}")
        add_project_to_json(folder_name, folder_path, use_git)

        if use_git:
            visibility = input("Do you want to make the repository public or private? (public/private): ").strip().lower()
            repo_name = input("Enter GitHub repository name (leave blank for default): ").strip() or folder_name
            visibility = visibility if visibility in ["public", "private"] else "private"

            if not create_github_repo(repo_name, visibility):
                rollback_project(folder_name, repo_name, use_git)
                return

            os.chdir(folder_path)
            subprocess.run(["git", "init"])
            subprocess.run(["git", "branch", "-M", "main"])
            subprocess.run(["git", "remote", "add", "origin", f"https://github.com/{GITHUB_USERNAME}/{repo_name}.git"])

            with open("README.md", "w") as readme:
                readme.write(f"# {repo_name}\n\nThis is the {repo_name} project.")

            subprocess.run(["git", "add", "."])
            subprocess.run(["git", "commit", "-m", "Initial commit"])
            subprocess.run(["git", "push", "-u", "origin", "main"])

            print(f"✅ GitHub repository '{repo_name}' created and linked to {folder_path}")
    except Exception as e:
        print(f"❌ Error: {e}")
        rollback_project(folder_name, repo_name if use_git else None, use_git)

def clone_project(repo_url, folder_name):
    if not folder_name:
        print("❌ Please provide a folder name.")
        return
    os.makedirs(CLONE_PATH, exist_ok=True)
    folder_path = os.path.join(CLONE_PATH, folder_name)
    if os.path.exists(folder_path):
        print(f"⚠️ Folder '{folder_name}' already exists in /clone. Choose a different name.")
        return
    try:
        print(f"🔄 Cloning repository from {repo_url} into {folder_path}...")
        subprocess.run(["git", "clone", repo_url, folder_path], check=True)
        add_project_to_json(folder_name, folder_path, True)
        print(f"✅ Repository cloned successfully into {folder_path}")
        open_project(folder_name)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to clone repository: {e}")

def create_github_repo(repo_name, visibility):
    if not GITHUB_TOKEN or not GITHUB_USERNAME:
        print("❌ GitHub credentials not found. Set GITHUB_TOKEN and GITHUB_USERNAME in environment variables.")
        return False

    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    data = {"name": repo_name, "private": visibility == "private"}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"🎉 Repository '{repo_name}' successfully created on GitHub!")
        return True
    else:
        print(f"❌ Failed to create repository: {response.json()}")
        return False

def rollback_project(folder_name, repo_name, use_git):
    folder_path = os.path.join(BASE_PATH, folder_name)
    if os.path.exists(folder_path):
        subprocess.run(["rm", "-rf", folder_path], check=True)
        print(f"🗑️ Removed folder: {folder_path}")
    if use_git and repo_name:
        delete_github_repo(repo_name)
    remove_project_from_json(folder_name)

def delete_github_repo(repo_name):
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"🗑️ Deleted GitHub repository: {repo_name}")
    else:
        print(f"⚠️ Failed to delete GitHub repository: {response.json()}")

def add_project_to_json(folder_name, folder_path, use_git):
    projects = load_json()
    projects[folder_name] = {"folder_path": folder_path, "use_git": use_git}
    save_json(projects)
    print(f"📄 Project '{folder_name}' added to projects.json")

def remove_project_from_json(folder_name):
    projects = load_json()
    if folder_name in projects:
        del projects[folder_name]
        save_json(projects)
        print(f"📄 Removed '{folder_name}' from projects.json")

def load_json():
    if os.path.exists(PROJECTS_JSON):
        with open(PROJECTS_JSON, "r") as file:
            return json.load(file)
    return {}

def save_json(data):
    with open(PROJECTS_JSON, "w") as file:
        json.dump(data, file, indent=4)

def open_project(folder_name):
    if not folder_name:
        print("❌ Please provide a folder name.")
        return

    # Check in BASE_PATH first
    folder_path = os.path.join(BASE_PATH, folder_name)
    if not os.path.exists(folder_path):
        # If not found, then check in CLONE_PATH
        folder_path = os.path.join(CLONE_PATH, folder_name)
        if not os.path.exists(folder_path):
            print(f"❌ Folder does not exist in either location: {os.path.join(BASE_PATH, folder_name)} or {os.path.join(CLONE_PATH, folder_name)}")
            return

    print(f"📂 Opening project: {folder_path}")
    subprocess.run(["code", folder_path], shell=True)
    print("🚀 Opened in VS Code!")

def list_projects():
    """ List all projects recorded in projects.json """
    projects = load_json()
    if not projects:
        print("❌ No projects found in projects.json.")
        return

    print("📄 Projects in projects.json:")
    for project, details in projects.items():
        print(f" - {project} -> {details['folder_path']} (Git: {'Yes' if details['use_git'] else 'No'})")

