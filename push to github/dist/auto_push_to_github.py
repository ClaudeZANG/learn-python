import subprocess
import os

def run_git_command(command):
    try:
        # Execute the Git command
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr}")

def main():
    # Change directory to the project folder
    os.chdir(r"C:\Users\chuan\OneDrive\s\PythonLearn")

    # Add all changes
    run_git_command(["git", "add", "."])

    # Commit changes
    commit_message = "Auto-commit from auto_push_to_github script"
    run_git_command(["git", "commit", "-m", commit_message])

    # Push changes to GitHub
    run_git_command(["git", "push", "origin", "master"])

if __name__ == "__main__":
    main()
