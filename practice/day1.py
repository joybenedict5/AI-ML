# Day 1 Exercise - Variables, strings, numbers, math

# --- Strings (text) ---
first_name = "Benne"
last_name = "Your Last Name"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# --- Numbers ---
age = 25
experience_years = 2
years_to_senior = 3
total_career = experience_years + years_to_senior
print("Total years of experience by then:", total_career)

# --- Math ---
monthly_salary_target = 100000
weekly = monthly_salary_target / 52
daily = weekly / 5
print("Daily earnings at target salary: $", round(daily, 2))

# --- Boolean (True or False) ---
has_pega_cert = True
has_python_skills = False  # not yet!
print("Do I have Pega cert?", has_pega_cert)
print("Do I have Python skills?", has_python_skills)

# --- Input from user ---
name = input("Type your name and press Enter: ")
print("Welcome to AI/ML journey,", name, "!")