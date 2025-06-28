import os
import openai
from openai import OpenAI
import json

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost",  # required by OpenRouter
        "X-Title": "HealthPay Backend Assignment"  # optional: project title
    }
)

def process_bill(text: str) -> dict:
    prompt = f"""
Extract the following fields from the bill text:
- hospital_name
- total_amount
- date_of_service (in YYYY-MM-DD format)

Respond ONLY in JSON like this:
{{
  "hospital_name": "...",
  "total_amount": 12345,
  "date_of_service": "2024-04-10"
}}

Text:
{text}
"""

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    try:
        return json.loads(response.choices[0].message.content.strip().lower())
    except json.JSONDecodeError:
        return {"error": "Failed to parse bill"}





# import openai
# import json

# def process_bill(text: str) -> dict:
#     prompt = f"""Extract this info from the bill: hospital_name, total_amount, and date_of_service.
# Return as JSON:
# {text}"""

#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     return json.loads(response["choices"][0]["message"]["content"])
