.PHONY: install
install: ## Install the virtual environment and  pre-commit hooks
	@echo "📦 Creating virtual environment"
	@pip install uv
	@uv venv
	@. .venv/bin/activate
	@echo "📦 Installing dependencies"
	@uv pip compile -o requirements.txt pyproject.toml
	@uv pip sync requirements.txt

.PHONY: install-dev
install-dev: ## Install the virtual environment and  pre-commit hooks
	@echo "📦 Creating virtual environment"
	@pip install uv
	@uv venv
	@echo "📦 Installing dependencies"
	@uv pip compile -o requirements.txt pyproject.toml
	@uv pip compile -o requirements-dev.txt --extra=dev pyproject.toml
	@uv pip sync requirements-dev.txt
	@. .venv/bin/activate
	@mypy --install-types

.PHONY: check
check: ## Run code quality tools.
	@echo "🔒 Compiling requirements from 'pyproject.toml':"
	@. .venv/bin/activate
	@uv pip compile -o requirements.txt pyproject.toml
	@uv pip compile -o requirements-dev.txt --extra=dev pyproject.toml
	@echo "🧹 Linting code: Running pre-commit"
	@echo "🔬 Static type checking: Running mypy"
	@mypy --install-types
	@mypy .

.PHONY: test
test: ## Test the code with pytest
	@echo "✅ Testing code: Running pytest"
	@. .venv/bin/activate
	@pytest --doctest-modules

.PHONY: docs
docs: ## Build and serve the documentation
	@source .venv/bin/activate
	@mkdocs serve

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	# TODO - implement

.PHONY: update	
update: ## Update pre-commit hooks
	@echo "⚙️ Updating environment and pre-commit hooks"
	@source .venv/bin/activate
	@pre-commit autoupdate

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
