import os
import openai
from dotenv import load_dotenv
from pathlib import Path
import time
from utils.label_maps import vertical_map

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

MAX_WRITES_PER_RUN = 404

audiences = {
    "customer": "Speak to them as IT admins or financial decision makers. Emphasise operational impact and cost justification.",
    "partner": "Help them pitch to customers. Explain pain points customers care about and how to position Meraki.",
    "internal": "Focus on partner enablement and supporting them in pitching to customers effectively."
}

verticals = list(vertical_map.keys())

products = ["mx", "mr", "ms", "mv", "mt", "sm", "mg"]
lengths = ["30min", "60min"]

base_path = Path("demo_flows")

def build_prompt(audience, vertical, product, length):
    time_scope = "two to three" if length == "30min" else "four to six"
    vertical_label = vertical_map[vertical]
    persona_instructions = audiences[audience]

    # Define tailored FAQ seed prompts (with answers)
    faq_tailoring = {
        "customer": f"""End the script with 2–3 frequently asked questions that a customer in the {vertical_label} sector might ask about {product.upper()}, along with short, clear answers. For example:
    Q: How does this solution reduce IT workload in our {vertical_label.lower()} environment?  
    A: Meraki simplifies management through one dashboard and automates many tasks like updates and troubleshooting.

    Q: What kind of ROI or cost reduction can we expect?  
    A: Customers often report major time savings and reduced downtime, especially for remote sites.

    Q: Can we integrate this with our existing systems and security policies?  
    A: Yes — Meraki supports APIs, SAML, and integration with existing firewalls, Active Directory, and SIEM tools.""",

        "partner": f"""End the script with 2–3 common questions a partner might ask when positioning {product.upper()} in the {vertical_label} space, each with a helpful answer. For example:
    Q: What are the top {vertical_label.lower()} pain points this addresses?  
    A: Usually lack of visibility, slow troubleshooting, and complexity managing multiple sites.

    Q: How do we best position {product.upper()} during the pitch?  
    A: Emphasise Meraki’s ease of use, single dashboard, and fast deployment with built-in security.

    Q: What installation or deployment concerns should we be ready for?  
    A: It’s typically plug-and-play, but partners should ensure licensing is pre-applied and templates are ready.""",

        "internal": f"""End the script with 2–3 internal enablement FAQs to support partners selling {product.upper()} in the {vertical_label} space. Each answer should be practical. For example:
    Q: What objections might the partner hear in {vertical_label.lower()}?  
    A: Cost vs legacy vendors, and skepticism over cloud-managed security — arm them with TCO comparisons.

    Q: What enablement do we provide for partners?  
    A: Access to demo kits, dashboards, playbooks, and partner-exclusive webinars.

    Q: How do we support onboarding post-sale?  
    A: We offer co-delivery workshops, pre-built config templates, and Meraki support handles escalations fast."""
    }


    return f"""
You are building a {length} demo script for Cisco Meraki.

Product: **{product.upper()}**  
Audience: **{audience.title()}**  
Sector: **{vertical_label}**

{persona_instructions}

Start with a short, friendly intro that reminds the presenter of:
- Who they are speaking to (e.g. partner reseller, customer IT admin, or internal SE)
- What the purpose of this demo is
- 1–2 warm-up questions tailored to the audience type:
    - For partners: What trends or challenges are you seeing with customers in this sector? What do you find unique or tricky about positioning solutions in this space?
    - For customers: What does your current network setup look like? Where are your biggest IT headaches today?
    - For internal: What common questions do our customers ask in the {vertical_label} sector? What objections or misconceptions do we frequently encounter?

Your script should:
- Focus on the specific needs of the **{vertical_label}** sector
- Include {time_scope} strong, specific use cases
- Use natural, spoken-style language — not formal marketing text
- Highlight the Meraki Dashboard as the central platform (single pane of glass)
- Emphasise how this enables visibility, simplified troubleshooting, and unified management
- Include at least {'2–3' if length == '30min' else '4–6'} UI interactions where the presenter would click or navigate the dashboard
- Format all UI actions with bold syntax (e.g., **click 'Configure > Switch ports'**)

{faq_tailoring[audience]}

Only return the demo script. No headings or extra intro text.
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

audiences_to_run = list(audiences.keys())
verticals_to_run = list(vertical_map.keys())
products_to_run = ["mx", "mr", "ms", "mv", "mt", "sm", "mg"]
lengths_to_run = ["30min", "60min"]
total = len(audiences_to_run) * len(verticals_to_run) * len(products_to_run) * len(lengths_to_run)
written = 0

for audience in audiences_to_run:
    for vertical in verticals_to_run:
        if audience == "customer" and vertical not in [
            "federal_gov", "finance", "healthcare", "higher_ed", "hospitality",
            "k12", "manufacturing", "professional_services", "retail", "service_provider",
            "small_business", "state_local_gov"
        ]:
            continue
        if audience != "customer":
            continue
        for product in products_to_run:
            for length in lengths_to_run:
                if written >= MAX_WRITES_PER_RUN:
                    print(f"\n🛑 Reached batch limit of {MAX_WRITES_PER_RUN}. Run again to continue.")
                    exit()

                folder = base_path / audience / vertical / product
                folder.mkdir(parents=True, exist_ok=True)
                path = folder / f"{length}.md"

                print(f"[OVERWRITE] {path}")

                prompt = build_prompt(audience, vertical, product, length)
                result = call_openai_with_retries(prompt)

                if not result:
                    print(f"[FAIL] {path}")
                    continue

                write_demo_flow(path, result)
                written += 1
                print(f"[{written}/{total}] ✅ Wrote → {path}")

print(f"\n✅ Session complete. {written} files written.")