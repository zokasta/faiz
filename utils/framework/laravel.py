import os
import subprocess

def main(args):
    if len(args) < 1:
        print("You must specify a project name")
        return

    project_name = args[0]
    github_repo = "https://github.com/zokasta/laravel.git"

    print("Cloning repository...")
    subprocess.run(["git", "clone", github_repo, project_name])

    os.chdir(project_name)

    print("Removing .git directory...")
    subprocess.run(["rm", "-rf", ".git"])

    print("Installing dependencies...")
    subprocess.run(["composer", "install"])

    print("Copying .env.example to .env...")
    subprocess.run(["cp", ".env.example", ".env"])

    print("Generating application key...")
    subprocess.run(["php", "artisan", "key:generate"])

    print(
        f"Project setup complete. Navigate to the {project_name} directory and start developing!"
    )
