import os

# Set the root of your project
project_root = os.path.abspath(os.getcwd())
snapshot_path = os.path.join(project_root, "project_snapshot.txt")

# File extensions to include
code_extensions = [".py", ".js", ".ts", ".html", ".css", ".sh", ".txt", ".yml", ".yaml"]

# Folders to exclude (case-sensitive)
excluded_dirs = {"demo_flows", "md", "__pycache__", "venv", "node_modules"}

# Files to exclude
excluded_extensions = {".md"}

with open(snapshot_path, "w", encoding="utf-8") as snapshot:
    snapshot.write(f"📁 Project Root: {project_root}\n\n")

    for foldername, subdirs, filenames in os.walk(project_root):
        # Skip any folder that is in excluded_dirs
        if any(excluded in foldername.split(os.sep) for excluded in excluded_dirs):
            continue

        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            ext = os.path.splitext(filename)[1]

            if ext in code_extensions and ext not in excluded_extensions:
                rel_path = os.path.relpath(filepath, project_root)
                snapshot.write(f"===== FILE: {rel_path} =====\n\n")
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        snapshot.write(f.read())
                except Exception as e:
                    snapshot.write(f"[Error reading file: {e}]\n")
                snapshot.write("\n\n")