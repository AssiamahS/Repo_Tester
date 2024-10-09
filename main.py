import os
import subprocess
import json

def clone_repo(repo_url, repo_dir):
    subprocess.run(["git", "clone", repo_url, repo_dir], check=True)

def run_tests(repo_dir):
    result = subprocess.run(["pytest", repo_dir], capture_output=True, text=True)
    return result.returncode == 0

def main():
    repo_url = os.getenv('REPO_URL')
    repo_dir = "/tmp/test_repo"

    try:
        clone_repo(repo_url, repo_dir)
        if run_tests(repo_dir):
            print("PASS: Repository tests passed.")
        else:
            print("FAIL: Repository tests failed.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
