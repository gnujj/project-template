# project-template

A lightweight Python project template using Poetry and GitHub Actions.

---

## 🚀 Quickstart

```bash
# Clone the template
git clone https://github.com/your-username/project-template.git
cd project-template

# Initialize project metadata (name, package, author, etc.)
python init_project.py

# Install dependencies
poetry install

# Run your CLI (renamed via init_project.py)
poetry run project-template
```

---

## 📁 Project Structure

```
.
├── project-template/        # Python package (renamed via init_project.py)
│   ├── __init__.py          # Contains __version__
│   └── main.py              # CLI entry point
├── pyproject.toml           # Project metadata & dependencies
├── bump_version.py          # Version bumping script
├── init_project.py          # One-time initializer
└── .github/workflows/
    └── bump-version.yml     # CI pipeline for versioning
```

---

## 🔖 Version Bumping (CI/CD)

Semantic versioning is powered by GitHub Actions:

- Push a commit to `main` with `[major]`, `[minor]`, or `[patch]` to trigger a version bump.
- The workflow:
  - updates `pyproject.toml` and `__init__.py`,
  - creates and pushes a Git tag,
  - commits updated files.

Alternatively, run the workflow manually from **GitHub → Actions → Bump Version → Run workflow** and select the bump level.

---

## ⚙ Customize Your Project

After running `init_project.py`, these fields will be updated automatically:

- Project name in `pyproject.toml`
- CLI entry point
- Python package folder
- Author name and email
- Mentions in `README.md`

---

## 🪄 Requirements

- Python ≥ 3.11
- [Poetry](https://python-poetry.org/docs/#installation)
- Git + GitHub

---

## 🧪 License

MIT — see [LICENSE](LICENSE)
