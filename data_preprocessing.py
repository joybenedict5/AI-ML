import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib

def generate_sample_data(n=1000):
    np.random.seed(42)
    df = pd.DataFrame({
        'income':         np.random.normal(60000, 20000, n).clip(20000, 200000),
        'credit_score':   np.random.normal(680, 80, n).clip(300, 850),
        'debt_to_income': np.random.normal(0.35, 0.15, n).clip(0.05, 0.95),
        'loan_amount':    np.random.normal(15000, 8000, n).clip(1000, 50000),
        'employment_years': np.random.normal(5, 3, n).clip(0, 30),
    })
    df['approved'] = (
        (df['credit_score'] > 650) &
        (df['debt_to_income'] < 0.45) &
        (df['income'] > 40000)
    ).astype(int)
    return df

def preprocess(df):
    features = ['income', 'credit_score', 'debt_to_income', 'loan_amount', 'employment_years']
    X = df[features]
    y = df['approved']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    joblib.dump(scaler, 'scaler.pkl')
    print("Scaler saved.")

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )
    return X_train, X_test, y_train, y_test, features

if __name__ == "__main__":
    df = generate_sample_data()
    X_train, X_test, y_train, y_test, features = preprocess(df)
    print(f"Train size: {len(X_train)} | Test size: {len(X_test)}")
    print("Class distribution:\n", df['approved'].value_counts())