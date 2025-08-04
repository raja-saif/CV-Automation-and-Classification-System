# whatsapp_sender.py
import pywhatkit as kit
import datetime
import time
from contacts import CONTACTS

DOMAIN_MESSAGES = {
    "AI": "Thank you for applying for the AI role. We’ll get back to you soon!",
    "Web Development": "Thanks for applying for the Web Dev position.",
    "HR": "Thanks for your interest in our HR team.",
    "Finance": "We received your application for the Finance role.",
    "Marketing": "Thanks for applying for our Marketing team.",
    "Data Science": "Thanks for your Data Science application.",
    "Unknown": "Thanks for applying. We’ll review your profile and contact you shortly."
}

def send_message(number, message, wait_seconds=20):
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute + 2  # ⬅️ Give 2 minutes buffer for WhatsApp web to load

    if minutes >= 60:
        minutes %= 60
        hours = (hours + 1) % 24

    try:
        print(f"Sending message to {number} at {hours}:{minutes}...")
        kit.sendwhatmsg(number, message, hours, minutes, wait_time=wait_seconds)
        print("✅ Message scheduled")
    except Exception as e:
        print(f"❌ Failed to send message to {number}: {e}")

def send_messages(results):
    print("📲 Sending WhatsApp replies...\n")
    for email, domain in results.items():
        number = CONTACTS.get(domain, CONTACTS.get("Default"))
        message = DOMAIN_MESSAGES.get(domain, DOMAIN_MESSAGES["Unknown"])
        send_message(number, message)
        time.sleep(5)  # Wait a bit before sending the next message
