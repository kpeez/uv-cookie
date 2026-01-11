#!/usr/bin/env python
from pathlib import Path
import shutil

PROJECT_DIRECTORY = Path.cwd()


def remove(filename: str | Path) -> None:
    """Remove a file or directory from the project."""
    try:
        filepath = next(PROJECT_DIRECTORY.rglob(f"{filename}"))
        if filepath.is_file():
            filepath.unlink()
        elif filepath.is_dir():
            shutil.rmtree(filepath)
    except StopIteration:
        # File/directory doesn't exist, skip
        pass


if __name__ == "__main__":
    if "{{cookiecutter.include_github_actions}}" != "y":
        remove(".github")

    if "{{cookiecutter.mkdocs}}" != "y":
        remove("docs")
        remove("mkdocs.yaml")

    if "{{cookiecutter.dockerfile}}" != "y":
        remove("Dockerfile")

    if "{{cookiecutter.codecov}}" != "y":
        remove("codecov.yaml")
        if "{{cookiecutter.include_github_actions}}" == "y":
            remove(".github/workflows/validate-codecov-config.yml")
