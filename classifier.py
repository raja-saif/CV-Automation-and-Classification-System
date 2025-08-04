# classifier.py
import os
import parser

DOMAINS = {
    "AI": ["machine learning", "deep learning", "neural network", "tensorflow", "pytorch", "nlp", "ai"],
    "Web Development": ["html", "css", "javascript", "react", "frontend", "backend", "django", "node"],
    "Finance": ["accounting", "finance", "banking", "financial analysis", "investment", "auditing"],
    "HR": ["recruitment", "payroll", "human resource", "employee relations", "hr policies"],
    "Marketing": ["seo", "social media", "branding", "content creation", "marketing campaign"],
    "Data Science": ["data analysis", "python", "statistics", "pandas", "data visualization", "regression"],
}

def classify_text(text):
    text = text.lower()
    scores = {domain: 0 for domain in DOMAINS}
    for domain, keywords in DOMAINS.items():
        for kw in keywords:
            if kw in text:
                scores[domain] += 1
    # Return the domain with highest score
    return max(scores, key=scores.get) if max(scores.values()) > 0 else "Unknown"

def classify_all(folder="attachments"):
    results = {}
    extracted = parser.process_attachments(folder)
    for fname, content in extracted.items():
        domain = classify_text(content)
        results[fname] = domain
    return results

if __name__ == "__main__":
    classified = classify_all()
    for fname, domain in classified.items():
        print(f"📄 {fname} → 🧠 Predicted Domain: {domain}")
