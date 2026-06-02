# Loan Decision Engine

An AI-powered loan approval system that combines machine learning with LLM-generated explanations to help lenders make fast, accurate, and explainable credit decisions.

## Features
- Logistic Regression model trained on income, credit score, and debt-to-income data
- 94% accuracy with strong ROC-AUC across all risk categories
- Stratified K-Fold cross-validation across imbalanced risk groups
- LangChain + Claude integration for plain-English decision explanations
- REST API built with Flask

## Tech Stack
Python · scikit-learn · LangChain · Flask · pandas · NumPy

## Setup
```bash
pip install -r requirements.txt
python model_training.py
python app.py
```

## API Usage
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "income": 75000,
    "credit_score": 720,
    "debt_to_income": 0.28,
    "loan_amount": 12000,
    "employment_years": 6
  }'
```

## Results
| Metric | Score |
|--------|-------|
| Accuracy | 94% |
| ROC-AUC | Strong across all risk tiers |
| False Negative Reduction | ~18% after fine-tuning |
| CV Reliability Improvement | ~12% via stratified k-fold |