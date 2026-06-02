# Mini Project - Simple Loan Checker
# This is the seed of your signature project!

print("=== Simple Loan Checker ===")
print("")

# Get input from user
name = input("Applicant name: ")
income = int(input("Monthly income ($): "))
loan_amount = int(input("Loan amount requested ($): "))
credit_score = int(input("Credit score (300-850): "))

# Simple decision rules
print("")
print("--- Analyzing application for", name, "---")

# Rule 1 - income check
if income >= 3000:
    income_check = "PASS"
else:
    income_check = "FAIL"

# Rule 2 - credit score check
if credit_score >= 650:
    credit_check = "PASS"
else:
    credit_check = "FAIL"

# Rule 3 - loan ratio check
ratio = loan_amount / income
if ratio <= 10:
    ratio_check = "PASS"
else:
    ratio_check = "FAIL"

# Print results
print("Income check:      ", income_check)
print("Credit score check:", credit_check)
print("Loan ratio check:  ", ratio_check)
print("")

# Final decision
if income_check == "PASS" and credit_check == "PASS" and ratio_check == "PASS":
    print("DECISION: ✓ APPROVED")
    print("next step: Trigger >> Loan_Disbursement stage")
elif credit_check == "FAIL":
    print("DECISION: ✗ REJECTED")
    print("next step: Trigger >> Manual_Review stage")
else:
    print("DECISION: ⚠ NEEDS REVIEW")
    print("next step: Trigger >> Document_Collection stage")