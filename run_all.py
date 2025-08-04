# run_all.py
import gmail_reader
import parser  # use your parser.py here

def run_all():
    print("🔁 Authenticating and reading emails...")
    service = gmail_reader.authenticate_gmail()
    candidates = gmail_reader.extract_email_data(service)

    print(f"✅ Found {len(candidates)} candidate(s).\n")

    if not candidates:
        print("📭 No new unread emails with CVs found.")
        return

    print("📥 Extracting text from CVs...\n")
    extracted = parser.process_attachments()

    for fname, content in extracted.items():
        print(f"\n📄 {fname} content:\n{'-'*40}\n{content[:1000]}...\n")  # Preview only
        with open(f"{fname}.txt", "w", encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    run_all()

import classifier  # Add this import

# After parsing and saving .txt files
print("\n🧠 Classifying CVs...\n")
classified = classifier.classify_all()

for fname, domain in classified.items():
    print(f"📄 {fname} → 🧠 {domain}")
import whatsapp_sender

print("\n📲 Sending WhatsApp replies...\n")
whatsapp_sender.send_messages(classified)

