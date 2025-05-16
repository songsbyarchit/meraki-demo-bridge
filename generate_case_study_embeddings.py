import json
import torch
from sentence_transformers import SentenceTransformer, util
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("case_studies.json") as f:
    case_studies = json.load(f)

if not os.path.exists("case_study_embeddings.json"):
    print("⚙️ Generating embeddings...")
    texts = [entry["text"] for entry in case_studies]
    embeddings = model.encode(texts, convert_to_numpy=True)
    with open("case_study_embeddings.json", "w") as f:
        json.dump(embeddings.tolist(), f)
        print(f"✅ Saved {len(embeddings)} embeddings to case_study_embeddings.json")

else:
    with open("case_study_embeddings.json") as f:
        embeddings = json.load(f)

case_embeddings = embeddings

def match_case_studies(query, top_k=3):
    query_embedding = model.encode(query, convert_to_tensor=True)
    with open("case_study_embeddings.json") as f:
        case_embeddings = json.load(f)
    embedding_tensor = torch.tensor(case_embeddings)
    hits = util.semantic_search(query_embedding, embedding_tensor, top_k=top_k)[0]
    matches = [case_studies[hit["corpus_id"]] for hit in hits]
    return matches