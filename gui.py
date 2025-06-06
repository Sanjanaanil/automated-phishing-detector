import tkinter as tk
from tkinter import messagebox
import joblib
from preprocess import clean_text

# Load model
model = joblib.load('saved_models/phishing_model.pkl')

def predict():
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)
    if not subject or not body.strip():
        messagebox.showwarning("Input Error", "Please enter both subject and body.")
        return
    text = clean_text(subject + " " + body)
    result = model.predict([text])[0]
    prediction = "Phishing Email" if result == 1 else "Legitimate Email"
    messagebox.showinfo("Result", prediction)

# GUI Setup
root = tk.Tk()
root.title("Phishing Email Detector")
root.geometry("400x300")

tk.Label(root, text="Email Subject:").pack(pady=5)
subject_entry = tk.Entry(root, width=50)
subject_entry.pack()

tk.Label(root, text="Email Body:").pack(pady=5)
body_text = tk.Text(root, height=10, width=50)
body_text.pack()

tk.Button(root, text="Detect", command=predict).pack(pady=10)

root.mainloop()
