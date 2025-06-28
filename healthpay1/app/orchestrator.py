from app.agents.classifier import classify_document
from app.agents.bill_agent import process_bill
from app.agents.discharge_agent import process_discharge

def orchestrate(text: str, filename: str):
    doc_type = classify_document(text, filename)

    if doc_type == "bill":
        return {"type": "bill", **process_bill(text)}
    elif doc_type == "discharge_summary":
        return {"type": "discharge_summary", **process_discharge(text)}
    else:
        return {"type": "unknown", "content": text}
