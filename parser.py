# parser.py
import os
import docx2txt
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading PDF {pdf_path}: {e}")
    return text

def extract_text_from_docx(docx_path):
    try:
        return docx2txt.process(docx_path)
    except Exception as e:
        print(f"Error reading DOCX {docx_path}: {e}")
        return ""

def process_attachments(folder="attachments"):
    extracted_data = {}
    for filename in os.listdir(folder):
        full_path = os.path.join(folder, filename)
        if filename.lower().endswith(".pdf"):
            extracted_data[filename] = extract_text_from_pdf(full_path)
        elif filename.lower().endswith(".docx"):
            extracted_data[filename] = extract_text_from_docx(full_path)
    return extracted_data

if __name__ == "__main__":
    data = process_attachments()
    for fname, content in data.items():
        print(f"--- {fname} ---\n{content[:1000]}...\n")  # printing only first 1000 chars
