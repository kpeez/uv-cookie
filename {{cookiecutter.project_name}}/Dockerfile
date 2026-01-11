FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev --no-install-project

# Copy source code
COPY {{cookiecutter.project_slug}} ./{{cookiecutter.project_slug}}/

# Install the project
RUN uv sync --frozen --no-dev

# Set entrypoint
ENTRYPOINT ["uv", "run", "python", "-m", "{{cookiecutter.project_slug}}"]
