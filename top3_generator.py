from sentence_transformers import SentenceTransformer, util
import json
from itertools import product
import torch
from cards.options_selector import VERTICAL_CHOICES, PRODUCT_LINE_CHOICES

VERTICALS = VERTICAL_CHOICES
PRODUCT_LINES = PRODUCT_LINE_CHOICES

# Load data
with open("case_studies.json", "r") as f:
    case_studies = json.load(f)

print(f"✅ Loaded {len(case_studies)} case studies.")

# Use case study 'text' field for embedding
case_texts = [case.get("text", "") for case in case_studies]
if not any(case_texts):
    print("⚠️ Warning: All case study texts are empty!")

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")
embedding_tensor = model.encode(case_texts, convert_to_tensor=True)
print("✅ Encoded all case study texts into embeddings.")

# Build top matches
top_case_studies = {}
combo_count = 0

for vertical, product in product(VERTICALS, PRODUCT_LINES):
    query = f"{vertical} {product}"
    query_embedding = model.encode(query, convert_to_tensor=True)
    similarities = util.cos_sim(query_embedding, embedding_tensor)[0]
    top_indices = similarities.argsort(descending=True)[:3]

    key = f"{vertical}|{product}"
    top_case_studies[key] = []

    for i in top_indices:
        case = case_studies[i]
        top_case_studies[key].append({
            "url": case.get("url", ""),
            "score": float(similarities[i])
        })
    
    print(f"🔹 Matched top 3 for: {key}")
    combo_count += 1

print(f"\n✅ Finished generating top case studies for {combo_count} vertical/product combinations.")

# Save result
with open("top_case_studies.json", "w") as f:
    json.dump(top_case_studies, f, indent=2)

print("✅ Saved top case studies to top_case_studies.json")