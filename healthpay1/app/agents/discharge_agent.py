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

def process_discharge(text: str) -> dict:
    prompt = f"""
Extract the following fields from the discharge summary:
- patient_name
- diagnosis
- admission_date (in YYYY-MM-DD format)
- discharge_date (in YYYY-MM-DD format)

Respond ONLY in JSON like this:
{{
  "patient_name": "...",
  "diagnosis": "...",
  "admission_date": "YYYY-MM-DD",
  "discharge_date": "YYYY-MM-DD"
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
        return {"error": "Failed to parse discharge summary"}




# import openai
# import json

# def process_discharge(text: str) -> dict:
#     prompt = f"""Extract this info: patient_name, diagnosis, admission_date, discharge_date.
# Return as JSON:
# {text}"""

#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     return json.loads(response["choices"][0]["message"]["content"])
