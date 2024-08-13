import subprocess
import os

def git_command(command):
    try:
        # Run the git command
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr}")

def update_study_folder():
    # Navigate to the project directory
    os.chdir(r"C:\Users\chuan\OneDrive\s")

    # Add all changes in the study folder
    git_command(["git", "add", "study/"])

    # Commit the changes with a message
    commit_message = "Auto-update study folder"
    git_command(["git", "commit", "-m", commit_message])

    # Push changes to the master branch on GitHub
    git_command(["git", "push", "origin", "master"])

if __name__ == "__main__":
    update_study_folder()
