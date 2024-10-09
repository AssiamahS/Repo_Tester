import os
import subprocess
import pytest

def clone_repo(repo_url, repo_dir):
    subprocess.run(["git", "clone", repo_url, repo_dir], check=True)

def run_tests(repo_dir):
    result = subprocess.run(["pytest", repo_dir], capture_output=True, text=True)
    return result.returncode == 0

@pytest.mark.parametrize("repo_url", [
    ("https://github.com/user/repo.git"),
])
def test_github_repo(repo_url):
    repo_dir = "/tmp/test_repo"
    clone_repo(repo_url, repo_dir)
    assert run_tests(repo_dir)
