# 📄 Resume Classifier & WhatsApp Auto-Responder

🚀 **Project:** Automated Resume Classification and WhatsApp Messaging  
🏢 **Internship:** CodeCelix – AI Internship (Day 1 Task)  
📅 **Start Date:** August 4, 2025  
👨‍💻 **Intern:** Raja Saif

---

## 📌 Project Overview

This project was assigned on Day 1 of my AI internship at [CodeCelix](https://www.linkedin.com/company/codecelix/). The goal was to automate the initial screening of resumes received via email and respond to applicants on WhatsApp based on the domain classification of their CVs.

---

## ✅ Features

- 📥 **Email Integration**  
  Automatically connects to Gmail and downloads unread attachments (PDF/DOCX).

- 📑 **Resume Parsing**  
  Extracts text content from PDF and DOCX formats using:
  - `pdfminer`
  - `python-docx`

- 🧠 **Resume Classification**  
  Trained a machine learning model (using `scikit-learn`) to classify resumes into categories like:
  - AI  
  - Web Development  
  - Data Science  
  - Default (others)

- 💬 **WhatsApp Auto-Messaging**  
  Sends personalized messages to candidates via WhatsApp using `pywhatkit`.

---

## 🧪 How It Works

1. Run the main script:
   ```bash
   python run_all.py
# CV-Automation-and-Classification-System
This project automates the end-to-end process of handling incoming job applications by integrating Gmail, AI-based resume classification, and WhatsApp messaging.
