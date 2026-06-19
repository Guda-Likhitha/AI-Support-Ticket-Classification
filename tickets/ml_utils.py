import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(
    BASE_DIR / "ml_model/model.pkl"
)

vectorizer = joblib.load(
    BASE_DIR / "ml_model/vectorizer.pkl"
)

def classify_ticket(text):

    transformed = vectorizer.transform([text])

    category = model.predict(transformed)[0]

    return category