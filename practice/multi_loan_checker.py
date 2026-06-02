# Multi Loan Checker - Day 2
# Upgraded from loan_checker.py - now handles multiple applicants!

# --- Applicant data (lists) ---
names =         ["Mahesh", "Priya",  "John",  "Sara",  "Ravi"]
incomes =       [90000,     25000,    55000,   120000,  40000]
loan_amounts =  [500000,    200000,   100000,  800000,  150000]
credit_scores = [920,       580,      700,     810,     640]

print("========================================")
print("      MULTI LOAN CHECKER SYSTEM         ")
print("========================================")
print("Total applications received:", len(names))
print("")

# --- Process each applicant using a loop ---
approved = 0
rejected = 0
review = 0

for i in range(len(names)):

    # Same rules as loan_checker.py
    income_check  = "PASS" if incomes[i] >= 3000 else "FAIL"
    credit_check  = "PASS" if credit_scores[i] >= 650 else "FAIL"
    ratio         = loan_amounts[i] / incomes[i]
    ratio_check   = "PASS" if ratio <= 10 else "FAIL"

    # Final decision
    if income_check == "PASS" and credit_check == "PASS" and ratio_check == "PASS":
        decision = "✓ APPROVED"
        pega_stage = "Loan_Disbursement"
        approved += 1
    elif credit_check == "FAIL":
        decision = "✗ REJECTED"
        pega_stage = "Manual_Review"
        rejected += 1
    else:
        decision = "⚠ NEEDS REVIEW"
        pega_stage = "Document_Collection"
        review += 1

    # Print result for each applicant
    print(f"Applicant : {names[i]}")
    print(f"Income    : ${incomes[i]}")
    print(f"Loan      : ${loan_amounts[i]}")
    print(f"Credit    : {credit_scores[i]}")
    print(f"Decision  : {decision}")
    print(f"Pega Step : Trigger >> {pega_stage} stage")
    print("----------------------------------------")

# --- Summary at the end ---
print("")
print("========== SUMMARY ==========")
print(f"Total Approved    : {approved}")
print(f"Total Rejected    : {rejected}")
print(f"Total Need Review : {review}")
print(f"Approval Rate     : {round(approved/len(names)*100)}%")
print("==============================")