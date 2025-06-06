✅ README.md
markdown
Copy
Edit
# 🛡️ Phishing Email Detector

This project is a simple machine learning-based tool to detect whether an email is **phishing** or **legitimate**, using Python and Natural Language Processing (NLP).

## 🚀 Features

- Preprocesses email subject and body text
- Trains a Naive Bayes classifier using TF-IDF
- GUI or CLI interface for predictions
- Saves trained model and vectorizer for reuse
- Simple dataset support and customizable input

## 🗂️ Project Structure

phishing_email_detector/
│
├── data/
│ └── phishing_dataset.csv # Input dataset (phishing vs legitimate)
│
├── saved_models/
│ ├── phishing_model.pkl # Trained ML model
│ └── tfidf_vectorizer.pkl # TF-IDF vectorizer
│
├── phishing_detector.py # Script to make predictions
├── train_model.py # Script to train the model
├── preprocess.py # Text preprocessing functions
├── gui.py # (Optional) GUI version using Tkinter
├── nltk_download.py # Downloads NLTK stopwords
├── README.md # Project overview
└── LICENSE # MIT License

perl
Copy
Edit

## 🧠 Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
If you don't have a requirements.txt, install manually:
bash
Copy
Edit
pip install pandas scikit-learn nltk joblib
🧪 Dataset Format
The dataset should be a .csv file with the following columns:

csv
Copy
Edit
Subject,Body,Label
"Win a free iPhone","Click here to claim",phishing
"Meeting update","Project discussion tomorrow at 10 AM",legitimate
Labels must be either:

phishing

legitimate

🏁 How to Run
1. Download NLTK stopwords (Run once)
bash
Copy
Edit
python nltk_download.py
2. Train the model
bash
Copy
Edit
python train_model.py
3. Predict via terminal
bash
Copy
Edit
python phishing_detector.py
4. (Optional) Run GUI
bash
Copy
Edit
python gui.py
📊 Sample Prediction
pgsql
Copy
Edit
Enter email subject: Important: Reset your password
Enter email body: Your account has been compromised. Click here to reset now.
Prediction: Phishing
