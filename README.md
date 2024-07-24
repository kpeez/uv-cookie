# cookiecutter-uv

My cookiecutter repo for generating python projects using `uv` for package management.

## Features

- [uv](https://github.com/astral-sh/uv) for package management
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Linting and formatting [ruff](https://github.com/charliermarsh/ruff) using the following rules:
  - pycodestyle
  - pyflakes
  - pylint
  - isort
  - flake8-bugbear
  - flake8-simplify
  - flake8-comprehensions
  - ruff

- Static type checking with [mypy](https://mypy.readthedocs.io/en/stable/)
- Publishing to [Pypi](https://pypi.org/)
- Testing with [pytest](https://docs.pytest.org/en/7.1.x/)
- Test coverage with [codecov](https://about.codecov.io/)
- Documentation with [MkDocs](https://www.mkdocs.org/)
- Containerization with [Docker](https://www.docker.com/)

## Usage

Make sure the `cookiecutter` package is installed:

```bash
pip install cookiecutter
```

Next, install the template directly from this repo:

```bash
cookiecutter https://github.com/kpeez/uv-cookie.git
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

## Acknowledgements

This was inspired by the [cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry) repo by [fpgmaas](https://github.com/fpgmaas).
I made some modifications to fit my personal use. Please check out fpgmaas' [cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry) for a more poetry-based comprehensive cookiecutter.
