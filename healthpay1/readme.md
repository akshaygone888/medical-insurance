# HealthPay Backend Developer Assignment

This project implements a simplified AI-driven medical claim processor API using FastAPI and OpenRouter (LLM API gateway). It receives medical claim PDF documents (bill, discharge summary, etc.), classifies them using a language model, extracts structured data using document-specific agents, validates the claim, and returns an approval or rejection decision.

---

## 🚀 Endpoint

### `POST /process-claim`

- Accepts: Multiple PDF files as `multipart/form-data`
- Returns: Structured JSON containing:
  - Document types + fields
  - Validation results
  - Final claim decision (approved/rejected with reason)

---

## 🧠 Architecture Overview

