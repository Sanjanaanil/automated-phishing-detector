import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
from preprocess import clean_text

# Load dataset
df = pd.read_csv('data/phishing_dataset.csv')

# Drop empty or missing rows
df.dropna(inplace=True)

# Optional: Clean column names and labels
df.columns = df.columns.str.strip()
df['Label'] = df['Label'].str.lower().str.strip().map({'phishing': 1, 'legitimate': 0})

# Combine subject and body
df['text'] = df['Subject'].astype(str) + " " + df['Body'].astype(str)
df['text'] = df['text'].apply(clean_text)

# Vectorize using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['Label']

# Train-test split with stratification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("\n✅ Model Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# Save model and vectorizer
os.makedirs("saved_models", exist_ok=True)
joblib.dump(model, "saved_models/phishing_model.pkl")
joblib.dump(vectorizer, "saved_models/tfidf_vectorizer.pkl")

print("\n✅ Model and vectorizer saved to 'saved_models/' folder.")

