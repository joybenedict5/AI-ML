import os

def explain_decision(prediction_result: dict) -> str:
    decision = prediction_result["decision"]
    prob = prediction_result["approval_probability"]
    applicant = prediction_result["applicant"]

    explanation = (
        f"Based on the applicant's income of ${applicant['income']:,}, "
        f"credit score of {applicant['credit_score']}, "
        f"and a debt-to-income ratio of {applicant['debt_to_income']}, "
        f"the loan application has been {decision.lower()} "
        f"with an approval probability of {prob}%. "
    )

    if decision == "Approved":
        explanation += "The applicant meets the required financial thresholds for loan approval."
    else:
        explanation += "The applicant does not meet one or more required financial thresholds."

    return explanation

if __name__ == "__main__":
    sample_result = {
        "decision": "Approved",
        "approval_probability": 87.5,
        "applicant": {
            "income": 75000,
            "credit_score": 720,
            "debt_to_income": 0.28,
            "loan_amount": 12000,
            "employment_years": 6
        }
    }
    print(explain_decision(sample_result))