import openai, os
openai.api_key = os.getenv("OPENAI_API_KEY")
def summarise_customer(purchases, vertical):
    prompt = f"Customer owns: {', '.join(purchases)}. Vertical: {vertical}. Suggest next demos, cross sells, and one case study."
    res = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                       messages=[{"role": "user", "content": prompt}])
    return res.choices[0].message.content.strip()