import pdfplumber

def extract_text_from_pdf(file) -> str:
    with pdfplumber.open(file.file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text
