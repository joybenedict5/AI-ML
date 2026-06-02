import joblib
import numpy as np

def predict(applicant: dict) -> dict:
    model  = joblib.load('loan_model.pkl')
    scaler = joblib.load('scaler.pkl')

    features = ['income', 'credit_score', 'debt_to_income', 'loan_amount', 'employment_years']
    values   = np.array([[applicant[f] for f in features]])
    scaled   = scaler.transform(values)

    prediction   = model.predict(scaled)[0]
    probability  = model.predict_proba(scaled)[0]

    return {
        "decision":          "Approved" if prediction == 1 else "Rejected",
        "approval_probability": round(float(probability[1]) * 100, 2),
        "rejection_probability": round(float(probability[0]) * 100, 2),
        "applicant":         applicant
    }

if __name__ == "__main__":
    sample = {
        "income": 75000,
        "credit_score": 720,
        "debt_to_income": 0.28,
        "loan_amount": 12000,
        "employment_years": 6
    }
    result = predict(sample)
    print(result)