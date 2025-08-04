import os
import base64
import json
import time
import fitz  # PyMuPDF for PDFs
import docx  # python-docx for .docx files

ATTACHMENTS_DIR = 'attachments/'

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

def extract_all_attachments():
    data = {}
    for filename in os.listdir(ATTACHMENTS_DIR):
        file_path = os.path.join(ATTACHMENTS_DIR, filename)
        if filename.endswith('.pdf'):
            data[filename] = extract_text_from_pdf(file_path)
        elif filename.endswith('.docx'):
            data[filename] = extract_text_from_docx(file_path)
    return data

if __name__ == "__main__":
    extracted = extract_all_attachments()
    for fname, content in extracted.items():
        print(f"\n📄 {fname} content:\n{'-'*40}\n{content[:1000]}...\n")  # Limit to 1000 chars
        with open(f"{fname}.txt", "w", encoding='utf-8') as f:
            f.write(content)

