import json
import os
from openai import OpenAI
from tqdm import tqdm

# Set your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load case studies
with open("case_studies.json", "r") as f:
    case_studies = json.load(f)

# Load top matches
with open("top_case_studies.json", "r") as f:
    top_case_studies = json.load(f)

# Create mapping from URL to case study text
url_to_text = {case["url"]: case.get("text", "") for case in case_studies}

# Loop through and summarise
seen = set()

for key, matches in tqdm(top_case_studies.items(), desc="Summarising"):
    for match in matches:
        if "summary" in match or match["url"] in seen:
            continue
        seen.add(match["url"])

        url = match["url"]
        full_text = url_to_text.get(url, "")
        if not full_text:
            match["summary"] = "⚠️ No content found to summarise."
            continue

        print(f"🔍 Summarising: {match['title']}")
        try:
            completion = client.chat.completions.create(
                model="gpt-4",  # or "gpt-3.5-turbo"
                messages=[
                    {"role": "system", "content": "You are a concise technical summariser."},
                    {"role": "user", "content": f"""Summarise this case study into 4–7 bullet points. Focus on results, key metrics, and outcomes. Keep as much of the original phrasing as possible. Only output bullet points:\n\n{full_text}"""}
                ],
                temperature=0.4
            )
            match["summary"] = completion.choices[0].message.content.strip()
        except Exception as e:
            print(f"❌ Failed to summarise {match['title']}: {e}")
            match["summary"] = f"⚠️ Error during summary: {str(e)}"

# Save back
with open("top_case_studies.json", "w") as f:
    json.dump(top_case_studies, f, indent=2)

print("✅ Summaries added to top_case_studies.json")