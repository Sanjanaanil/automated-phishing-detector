import joblib
from preprocess import clean_text

def predict_email(subject, body):
    model = joblib.load('saved_models/phishing_model.pkl')
    vectorizer = joblib.load('saved_models/tfidf_vectorizer.pkl')

    input_text = clean_text(subject + " " + body)
    input_vector = vectorizer.transform([input_text])
    prediction = model.predict(input_vector)

    return "Phishing" if prediction[0] == 1 else "Legitimate"

if __name__ == "__main__":
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")
    result = predict_email(subject, body)
    print("Prediction:", result)
