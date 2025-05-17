import json

# === Step 1: Load JSON ===
with open("top_case_studies.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# === Step 2: Build title → summary map (only non-empty summaries) ===
title_to_summary = {}
for section in data.values():
    for entry in section:
        title = entry.get("title")
        summary = entry.get("summary", "").strip()
        if title and summary:
            title_to_summary[title] = summary

# === Step 3: Fill missing summaries using title match ===
filled_count = 0
for section in data.values():
    for entry in section:
        title = entry.get("title")
        summary = entry.get("summary", "").strip()
        if title and not summary and title in title_to_summary:
            entry["summary"] = title_to_summary[title]
            filled_count += 1

# === Step 4: Save updated file (overwrite same file) ===
with open("top_case_studies.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Filled {filled_count} missing summaries based on matching titles. Output written to 'top_case_studies.json'.")
