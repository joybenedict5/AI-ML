import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report
from data_preprocessing import generate_sample_data, preprocess

def train():
    df = generate_sample_data()
    X_train, X_test, y_train, y_test, features = preprocess(df)

    model = LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced')

    # Stratified K-Fold Cross Validation
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = cross_val_score(model, X_train, y_train, cv=skf, scoring='roc_auc')
    print(f"Cross-Validation ROC-AUC Scores: {cv_scores}")
    print(f"Mean CV ROC-AUC: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_proba)

    print(f"\nTest Accuracy : {accuracy:.4f}")
    print(f"Test ROC-AUC  : {auc:.4f}")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    joblib.dump(model, 'loan_model.pkl')
    print("Model saved as loan_model.pkl")

if __name__ == "__main__":
    train()