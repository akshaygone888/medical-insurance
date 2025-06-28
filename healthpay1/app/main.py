from fastapi import FastAPI, UploadFile, File
from typing import List
from app.utils.pdf_utils import extract_text_from_pdf
from app.orchestrator import orchestrate
from app.agents.validator import validate_output, make_claim_decision

app = FastAPI()

@app.post("/process-claim")
async def process_claim(files: List[UploadFile] = File(...)):
    documents = []

    for file in files:
        text = extract_text_from_pdf(file)
        result = orchestrate(text, file.filename)
        documents.append(result)

    validation = validate_output(documents)
    decision = make_claim_decision(validation)

    return {
        "documents": documents,
        "validation": validation,
        "claim_decision": decision
    }
