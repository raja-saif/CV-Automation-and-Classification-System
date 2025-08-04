import tkinter as tk
from tkinter import messagebox
import threading
import run_all

def run_pipeline():
    try:
        status_label.config(text="🔁 Running full CV pipeline...")
        run_all.run_all()
        status_label.config(text="✅ All tasks completed successfully!")
        messagebox.showinfo("Done", "CVs processed and messages sent!")
    except Exception as e:
        status_label.config(text="❌ An error occurred")
        messagebox.showerror("Error", str(e))

def start_thread():
    threading.Thread(target=run_pipeline, daemon=True).start()

# GUI setup
root = tk.Tk()
root.title("CV Processor & WhatsApp Notifier")
root.geometry("400x250")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

heading = tk.Label(frame, text="CV Classifier & WhatsApp Sender", font=("Arial", 14, "bold"))
heading.pack(pady=10)

start_button = tk.Button(frame, text="Run Full Pipeline", command=start_thread, bg="#4CAF50", fg="white", padx=10, pady=5)
start_button.pack(pady=10)

status_label = tk.Label(frame, text="Idle", font=("Arial", 10), fg="gray")
status_label.pack(pady=10)

quit_button = tk.Button(frame, text="Exit", command=root.quit, bg="gray", fg="white", padx=10, pady=5)
quit_button.pack(pady=5)

root.mainloop()
