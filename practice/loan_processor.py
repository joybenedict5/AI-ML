# loan_processor.py
# Day 3 - Functions and Dictionaries
# Upgraded: each applicant is now a proper data record!

# --- DICTIONARIES --- (like a Pega case record!)
applicant1 = {
    "name": "Mahesh",
    "income": 90000,
    "loan_amount": 500000,
    "credit_score": 920,
    "employment": "Employed"
}

applicant2 = {
    "name": "Priya",
    "income": 25000,
    "loan_amount": 200000,
    "credit_score": 580,
    "employment": "Self-Employed"
}

applicant3 = {
    "name": "John",
    "income": 55000,
    "loan_amount": 100000,
    "credit_score": 700,
    "employment": "Employed"
}

# List of all applicants (list of dictionaries!)
all_applicants = [applicant1, applicant2, applicant3]

# --- FUNCTIONS --- (reusable code blocks)

def check_income(income):
    if income >= 3000:
        return "PASS"
    else:
        return "FAIL"

def check_credit(credit_score):
    if credit_score >= 650:
        return "PASS"
    else:
        return "FAIL"

def check_ratio(loan_amount, income):
    ratio = loan_amount / income
    if ratio <= 10:
        return "PASS"
    else:
        return "FAIL"

def get_pega_stage(decision):
    stages = {
        "APPROVED": "Loan_Disbursement",
        "REJECTED": "Manual_Review",
        "REVIEW":   "Document_Collection"
    }
    return stages[decision]

def process_application(applicant):
    """Main function - processes one applicant completely"""
    
    name         = applicant["name"]
    income       = applicant["income"]
    loan_amount  = applicant["loan_amount"]
    credit_score = applicant["credit_score"]
    employment   = applicant["employment"]

    # Run all checks
    income_check = check_income(income)
    credit_check = check_credit(credit_score)
    ratio_check  = check_ratio(loan_amount, income)

    # Make decision
    if income_check == "PASS" and credit_check == "PASS" and ratio_check == "PASS":
        decision   = "APPROVED"
        symbol     = "✓"
    elif credit_check == "FAIL":
        decision   = "REJECTED"
        symbol     = "✗"
    else:
        decision   = "REVIEW"
        symbol     = "⚠"

    pega_stage = get_pega_stage(decision)

    # Return result as a dictionary
    result = {
        "name":       name,
        "decision":   decision,
        "symbol":     symbol,
        "pega_stage": pega_stage,
        "checks": {
            "income":  income_check,
            "credit":  credit_check,
            "ratio":   ratio_check
        }
    }
    return result

# --- PROCESS ALL APPLICANTS ---
print("=" * 45)
print("      LOAN PROCESSOR v3.0 - WITH FUNCTIONS  ")
print("=" * 45)

results = []

for applicant in all_applicants:
    result = process_application(applicant)
    results.append(result)

    print(f"\nApplicant : {result['name']}")
    print(f"Income Ck : {result['checks']['income']}")
    print(f"Credit Ck : {result['checks']['credit']}")
    print(f"Ratio  Ck : {result['checks']['ratio']}")
    print(f"Decision  : {result['symbol']} {result['decision']}")
    print(f"Pega Step : Trigger >> {result['pega_stage']} stage")
    print("-" * 45)

# --- SUMMARY ---
approved = sum(1 for r in results if r["decision"] == "APPROVED")
rejected = sum(1 for r in results if r["decision"] == "REJECTED")
review   = sum(1 for r in results if r["decision"] == "REVIEW")

print(f"\n{'=' * 45}")
print(f"  SUMMARY")
print(f"{'=' * 45}")
print(f"  Approved : {approved}")
print(f"  Rejected : {rejected}")
print(f"  Review   : {review}")
print(f"  Rate     : {round(approved/len(results)*100)}%")
print(f"{'=' * 45}")