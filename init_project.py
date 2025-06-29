import re
from pathlib import Path

def replace_in_file(filepath, replacements):
    text = Path(filepath).read_text(encoding="utf-8")
    for pattern, repl in replacements.items():
        text = re.sub(pattern, repl, text)
    Path(filepath).write_text(text, encoding="utf-8")

def prompt(label, default=None):
    value = input(f"{label}" + (f" [{default}]" if default else "") + ": ").strip()
    return value or default

def main():
    print("🛠 Python Project Initializer\n")

    project_name = prompt("📝 Project name (e.g. my-awesome-tool)")
    if not project_name:
        print("❌ Project name is required.")
        return

    package_name = project_name.replace("-", "_")
    author = prompt("👤 Author name")
    email = prompt("📧 Author email")

    print("\n📦 Applying changes...")

    replace_in_file("pyproject.toml", {
        r'name = "project-template"': f'name = "{project_name}"',
        r'project-template = "project_template\.main:main"': f'{project_name} = "{package_name}.main:main"',
        r'name = "Your Name"': f'name = "{author}"',
        r'email = "you@example.com"': f'email = "{email}"',
    })

    replace_in_file("README.md", {
        r'project-template': project_name,
        r'project_template': package_name,
        r'your-username': author,
    })

    if Path("project_template").exists():
        Path("project_template").rename(package_name)

    print(f"\n✅ Done! Project initialized as `{project_name}` with package `{package_name}`. Author: {author} <{email}>.\n")

if __name__ == "__main__":
    main()
