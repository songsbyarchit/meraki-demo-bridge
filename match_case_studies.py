import json
import torch
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("case_studies.json") as f:
    case_studies = json.load(f)

with open("case_study_embeddings.json") as f:
    case_embeddings = json.load(f)

def match_case_studies(query, top_k=3):
    query_embedding = model.encode(query, convert_to_tensor=True)

    # Convert list of lists to tensor
    embedding_tensor = torch.tensor(case_embeddings)

    hits = util.semantic_search(query_embedding, embedding_tensor, top_k=top_k)[0]
    matches = [case_studies[hit["corpus_id"]] for hit in hits]

    return matches