import json

# Load once at import
with open("top_case_studies.json", "r") as f:
    STATIC_CASE_STUDIES = json.load(f)

def get_static_case_studies(vertical: str, product_line: str):
    key = f"{vertical}|{product_line}"
    return STATIC_CASE_STUDIES.get(key, [])