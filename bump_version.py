# bump_version.py

import re
from pathlib import Path
import sys
import tomllib  # Requires Python 3.11+

def read_package_name() -> str:
    pyproject = Path("pyproject.toml")
    data = tomllib.loads(pyproject.read_text("utf-8"))
    return data["project"]["name"].replace("-", "_")

def read_version(init_path: Path) -> str:
    content = init_path.read_text("utf-8")
    match = re.search(r'__version__\s*=\s*"([^"]+)"', content)
    if not match:
        raise ValueError("Couldn't find __version__ in __init__.py")
    return match.group(1)

def bump(version: str, level: str) -> str:
    major, minor, patch = map(int, version.split("."))
    if level == "major":
        return f"{major + 1}.0.0"
    elif level == "minor":
        return f"{major}.{minor + 1}.0"
    elif level == "patch":
        return f"{major}.{minor}.{patch + 1}"
    else:
        raise ValueError("Invalid level. Use: major, minor or patch")

def update_file(path: Path, pattern: str, replacement: str):
    content = path.read_text("utf-8")
    updated = re.sub(pattern, replacement, content)
    path.write_text(updated, encoding="utf-8")

def main():
    if len(sys.argv) != 2:
        print("Usage: python bump_version.py [major|minor|patch|--print-package]")
        sys.exit(1)

    arg = sys.argv[1].lower()

    if arg == "--print-package":
        package_name = read_package_name()
        print(package_name)
        sys.exit(0)

    if arg == "--print-version":
        package_name = read_package_name()
        init_path = Path(package_name) / "__init__.py"
        current_version = read_version(init_path)
        print(current_version)
        sys.exit(0)

    package_name = read_package_name()
    init_path = Path(package_name) / "__init__.py"
    pyproject_path = Path("pyproject.toml")

    current_version = read_version(init_path)
    new_version = bump(current_version, arg)

    print(f"🔧 Bumping version: {current_version} → {new_version}")

    update_file(init_path, r'__version__\s*=\s*"[^"]+"', f'__version__ = "{new_version}"')
    update_file(pyproject_path, r'version\s*=\s*"[^"]+"', f'version = "{new_version}"')

    print("✅ Version updated successfully.")

if __name__ == "__main__":
    main()
