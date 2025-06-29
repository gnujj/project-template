# project-template

A lightweight Python project template using Poetry and GitHub Actions.

---

## 🚀 Quickstart

```bash
# Install dependencies
poetry install

# Run the main CLI script
poetry run project-template
```

---

## 📁 Project Structure

```
.
├── project_template/       # Main Python package
│   ├── __init__.py         # Contains __version__
│   └── main.py             # CLI entry point
├── pyproject.toml          # Project metadata & dependencies
├── bump_version.py         # Semantic versioning tool
└── .github/workflows/
    └── bump-version.yml    # CI version auto-bump
```

---

## 🔖 Version Bumping

Commit messages on `main` that include `[patch]`, `[minor]`, or `[major]` will automatically trigger:

- version bump in `pyproject.toml` and `__init__.py`,
- git tag creation (e.g. `v0.2.0`),
- commit + push of changes.

You can also trigger it manually via GitHub → **Actions → Bump Version → Run workflow** with a selected bump level.

---

## ⚙ Configuration

To customize the project:

1. Update the package name in `pyproject.toml`:

   ```toml
   name = "your-project-name"
   ```

2. Rename the package folder:

   ```bash
   mv project_template your_project_name
   ```

3. Update CLI entry point in `pyproject.toml`:

   ```toml
   [project.scripts]
   your-cli = "your_project_name.main:main"
   ```

4. Set your author details:

   ```toml
   authors = [
       { name = "Your Name", email = "you@example.com" },
   ]
   ```

---

## 📦 Tech Stack

- Python ≥ 3.11
- [Poetry](https://python-poetry.org/) ≥ 1.8
- GitHub Actions (for CI and versioning)

