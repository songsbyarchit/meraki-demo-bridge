import os
import openai
from dotenv import load_dotenv
from pathlib import Path
import time

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

MAX_WRITES_PER_RUN = 404

audiences = {
    "customer": "Speak to them as IT admins or financial decision makers. Emphasise operational impact and cost justification.",
    "partner": "Help them pitch to customers. Explain pain points customers care about and how to position Meraki.",
    "internal": "Focus on partner enablement and supporting them in pitching to customers effectively."
}

verticals = [
    "k12", "healthcare", "manufacturing", "higher_ed", "hospitality", "retail",
    "federal_gov", "service_provider", "finance", "small_business", "state_local_gov", "professional_services"
]

products = ["mx", "mr", "ms", "mv", "mt", "sm", "mg"]
lengths = ["30min", "60min"]

base_path = Path("demo_flows")

def build_prompt(audience, vertical, product, length):
    time_scope = "two to three" if length == "30min" else "four to six"
    return f"""
Write a {length} demo script for a Meraki {product.upper()} demo, targeting the {vertical.replace("_", " ").title()} sector.
Audience type: {audience.title()}.

{audiences[audience]}

Include {time_scope} clear use cases. Use plain, natural speech, not marketing fluff.
Whenever a UI action is mentioned, write it like **click 'Configure > Switch ports'** so it's easy to follow.

End with two or three smart questions the presenter can ask the attendee to prompt discussion.
"""

def write_demo_flow(path, content):
    path.write_text(content.strip())

def call_openai_with_retries(prompt, retries=3):
    for attempt in range(retries):
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"[RETRY {attempt + 1}] Error: {e}")
            time.sleep(2)
    return None

written = 0
total = len(audiences) * len(verticals) * len(products) * len(lengths)

for audience in audiences:
    for vertical in verticals:
        for product in products:
            for length in lengths:
                if written >= MAX_WRITES_PER_RUN:
                    print(f"\n🛑 Reached batch limit of {MAX_WRITES_PER_RUN}. Run again to continue.")
                    exit()

                folder = base_path / audience / vertical / product
                folder.mkdir(parents=True, exist_ok=True)
                path = folder / f"{length}.md"

                if path.exists() and path.stat().st_size > 0:
                    print(f"[SKIP]    {path} already has content")
                    continue
                else:
                    print(f"[WRITE]   {path}")


                prompt = build_prompt(audience, vertical, product, length)
                result = call_openai_with_retries(prompt)

                if not result:
                    print(f"[FAIL] {path}")
                    continue

                write_demo_flow(path, result)
                written += 1
                print(f"[{written}/{total}] ✅ Wrote → {path}")

print(f"\n✅ Session complete. {written} files written.")