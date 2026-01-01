# problem-solving

Development notes and `uv` commands for running tests and installing dev dependencies.

Requirements

- A project-local virtual environment (the workspace uses `.venv`).
- `uv` package manager installed (optional but recommended).

Common `uv` workflows

1. Add dev dependencies (pytest, linters):

```bash
uv add --dev pytest ruff pre-commit
```

2. Install the project in editable mode (so `src/` is importable):

```bash
uv run python -m pip install -e .
```

3. Run tests inside the `uv` environment:

```bash
uv run pytest
# or
uv run python -m pytest
```

If you prefer not to use `uv`, activate the `.venv` and install manually:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .
pip install pytest
pytest
```

CI recommendation

- Use `uv` (or pip) to install dev deps, then run `uv run pytest` in your CI steps.

Notes

- Editable install (`pip install -e .`) is preferred over hacking `PYTHONPATH`.
- `pyproject.toml` contains a `build-system` section so editable installs work with modern pip.
