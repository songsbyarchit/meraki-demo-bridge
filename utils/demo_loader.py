from pathlib import Path

base_path = Path("demo_flows")

def get_demo_flow(audience, vertical, product, length):
    path = base_path / audience / vertical / product / f"{length}min.md"
    return path.read_text()