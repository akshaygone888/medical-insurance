import os
import openai
from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost",  # required by OpenRouter
        "X-Title": "HealthPay Backend Assignment"  # optional: project title
    }
)

def classify_document(text: str, filename: str) -> str:
    prompt = f"""
You are a document classifier. Given the filename and content, classify the document into one of these types:
- bill
- discharge_summary
- id_card

Return ONLY the type (bill, discharge_summary, or id_card).

Filename: {filename}

Content:
{text[:1000]}
"""

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    result = response.choices[0].message.content.strip().lower()
    return result



# import openai

# def classify_document(text: str, filename: str) -> str:
#     prompt = f"""Classify this document as one of: bill, discharge_summary, or id_card.
# Filename: {filename}
# Text: {text[:1000]}"""  # Cut long text to avoid token limit

#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     return response["choices"][0]["message"]["content"].strip().lower()
