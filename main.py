import os
from pathlib import Path

from github import Github


def main():
    about = {}
    with Path(os.environ["INPUT_PATH"]).open() as f:
        exec(f.read(), about)

    prefix = os.environ["INPUT_PREFIX"]
    variable = os.environ["INPUT_VARIABLE"]
    suffix = os.environ["INPUT_SUFFIX"]
    version_tag = f"{prefix}{about[variable]}{suffix}"

    g = Github(os.environ["GITHUB_TOKEN"] or os.environ["INPUT_GITHUB_TOKEN"])
    repo = g.get_repo(os.environ["github"]["repository"])

    for tag in repo.get_tags():
        if tag.name == version_tag:
            return

    sha = repo.get_commits()[0].sha
    repo.create_git_ref(f"refs/tags/{version_tag}", sha)


if __name__ == "__main__":
    main()
