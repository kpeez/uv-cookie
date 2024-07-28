# {{cookiecutter.project_name}}

[![License](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})

{{cookiecutter.project_description}}

- **Github repository**: <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>
- **Documentation** <https://{{cookiecutter.author_github_handle}}.github.io/{{cookiecutter.project_name}}/>

## Table of Contents  <!-- omit in toc -->

- [Installation](#installation)

## Installation

The easiest way to install the package is using the `make install` recipe in the `Makefile`.

```bash
git clone <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>
cd {{cookiecutter.project_slug}}
make install
```

> **Note:** The package uses `uv` (<https://github.com/astral-sh/uv>) for python package installation and dependency resolution. If you wish to use `pip` for package installation, you can use the `requirements.txt` file to install the dependencies.

```bash
git clone <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>
cd {{cookiecutter.project_slug}}
python -m venv .venv
pip install -r requirements.txt
pip install -e .
```

If you are developing the package, you can install it in development mode using the `make install-dev` recipe in the `Makefile`.

```bash
git clone <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>
cd {{cookiecutter.project_slug}}
make install-dev
```
