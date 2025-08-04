# gmail_reader.py
import os.path
import base64
import mimetypes
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def extract_email_data(service):
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q='is:unread').execute()
    messages = results.get('messages', [])
    candidates = []

    for msg in messages:
        msg_id = msg['id']
        message = service.users().messages().get(userId='me', id=msg_id).execute()
        headers = message['payload']['headers']
        from_header = next(h['value'] for h in headers if h['name'] == 'From')
        name, email = parse_email(from_header)

        parts = message['payload'].get('parts', [])
        for part in parts:
            if 'filename' in part and part['filename']:
                filename = part['filename']
                if filename.endswith('.pdf') or filename.endswith('.docx'):
                    data = part['body'].get('data')
                    attachment_id = part['body'].get('attachmentId')

                    if not data and attachment_id:
                        attachment = service.users().messages().attachments().get(
                            userId='me', messageId=msg_id, id=attachment_id).execute()
                        data = attachment.get('data')

                    if data:
                        file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
                        save_path = os.path.join("attachments", filename)
                        os.makedirs("attachments", exist_ok=True)
                        with open(save_path, "wb") as f:
                            f.write(file_data)

                        candidates.append({
                            "name": name,
                            "email": email,
                            "cv_path": save_path
                        })

    return candidates

def parse_email(header):
    if "<" in header:
        name = header.split("<")[0].strip().strip('"')
        email = header.split("<")[1].replace(">", "").strip()
    else:
        name = email = header
    return name, email

if __name__ == "__main__":
    service = authenticate_gmail()
    candidates = extract_email_data(service)
    for c in candidates:
        print(f"Name: {c['name']}, Email: {c['email']}, CV: {c['cv_path']}")
