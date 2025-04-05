# uv-mypy-template

A Python project template using `uv` for package management, `ruff` for formatting/linting, `mypy` for type checking, and `unittest` for testing.

## Purpose

This template provides a standardized starting point for new Python projects, pre-configured with modern development tools and best practices, including:

*   **Package Management:** Using `uv` (via `pyproject.toml` and `uv.lock`).
*   **Formatting & Linting:** Using `ruff`.
*   **Type Checking:** Using `mypy` with a strict configuration.
*   **Testing:** Using the built-in `unittest` framework.
*   **VS Code Integration:** Settings for test discovery and `PYTHONPATH`.
*   **CI/CD:** GitHub Actions workflow for running tests and quality checks on Pull Requests.

## Prerequisites

*   Python >= 3.12
*   `uv` installed (See [uv installation guide](https://github.com/astral-sh/uv#installation))

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone <repository-url> your-project-name
    cd your-project-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    uv venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3.  **Install dependencies (including development tools):**
    ```bash
    # Sync with the lock file (recommended for reproducibility)
    uv pip sync uv.lock
    # Or, install from pyproject.toml if you prefer/modified it
    # uv pip install -e .[dev]
    ```

## Development Workflow

### Formatting

To automatically format your code according to `ruff` rules:

```bash
uv run ruff format .
```

### Linting

To check for style issues and potential errors:

```bash
uv run ruff check .
```

### Type Checking

To perform static type checking with `mypy`:

```bash
uv run mypy src tests
```

### Running Tests

Tests are located in the `tests/` directory and use the `unittest` framework.

*   **Command Line:**
    ```bash
    # Discover and run all tests in the 'tests' directory
    uv run python -m unittest discover tests
    ```
*   **VS Code:** The included `.vscode/settings.json` and `.env` files configure the VS Code Python extension to discover and run tests via the Test Explorer UI. Ensure you have selected the project's virtual environment interpreter.

## Project Structure

```
.github/
└── workflows/
    └── python-tests.yml  # GitHub Actions CI workflow
src/
└── <your_package_name>/   # Your main application code
    └── __init__.py
tests/
└── <your_package_name>/   # Tests mirroring the src structure
    └── __init__.py
.env                   # Sets PYTHONPATH for VS Code test discovery
.gitignore             # Standard Python gitignore
.pre-commit-config.yaml # Configuration for pre-commit hooks (ruff, mypy)
.vscode/
└── settings.json      # VS Code settings for Python testing
README.md              # This file
 pyproject.toml         # Project metadata, dependencies, tool config (ruff, mypy)
uv.lock                # Pinned dependencies managed by uv
```

## Continuous Integration (CI)

A GitHub Actions workflow is configured in `.github/workflows/python-tests.yml`. It automatically runs linters, type checks, and unit tests on multiple Python versions for every Pull Request targeting the `main` or `develop` branches.
