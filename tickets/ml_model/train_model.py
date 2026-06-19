import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = {
    'ticket': [
        'payment failed',
        'refund request',
        'unable to login',
        'website crash',
        'account locked',
        'money deducted'
    ],

    'category': [
        'Billing',
        'Refund',
        'Account',
        'Technical',
        'Account',
        'Billing'
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df['ticket'])

model = LogisticRegression()

model.fit(X, df['category'])

joblib.dump(
    model,
    'tickets/ml_model/model.pkl'
)

joblib.dump(
    vectorizer,
    'tickets/ml_model/vectorizer.pkl'
)

print("Model Saved")