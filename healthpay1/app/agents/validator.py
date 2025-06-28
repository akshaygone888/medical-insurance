def validate_output(documents):
    types = [doc["type"] for doc in documents]
    missing = []

    if "bill" not in types:
        missing.append("bill")
    if "discharge_summary" not in types:
        missing.append("discharge_summary")

    return {
        "missing_documents": missing,
        "discrepancies": []
    }

def make_claim_decision(validation):
    if not validation["missing_documents"]:
        return {"status": "approved", "reason": "All required documents are present"}
    else:
        return {"status": "rejected", "reason": f"Missing: {validation['missing_documents']}"}
