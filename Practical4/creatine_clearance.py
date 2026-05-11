# Pseudocode:
# 1. Get age, weight, gender, creatinine from user
# 2. Validate input ranges:
#    age < 100, weight between 20 and 80, creatinine between 0 and 100,
#    gender either male or female
# 3. If valid, calculate CrCl = ((140 - age) * weight) / (72 * creatinine)
# 4. Multiply by 0.85 if female
# 5. Print result or error message

age = int(input("Enter age (years): "))
weight = float(input("Enter weight (kg): "))
gender = input("Enter gender (male/female): ").strip().lower()
creatinine = float(input("Enter creatinine concentration (umol/l): "))

valid = True
error_msg = ""

if age >= 100:
    valid = False
    error_msg += "Age must be less than 100.\n"
if weight <= 20 or weight >= 80:
    valid = False
    error_msg += "Weight must be between 20 and 80 kg.\n"
if creatinine <= 0 or creatinine >= 100:
    valid = False
    error_msg += "Creatinine must be between 0 and 100 umol/l.\n"
if gender not in ["male", "female"]:
    valid = False
    error_msg += "Gender must be male or female.\n"

if not valid:
    print("Input error:\n", error_msg)
else:
    crcl = ((140 - age) * weight) / (72 * creatinine)
    if gender == "female":
        crcl *= 0.85
    print(f"Creatinine clearance (CrCl): {crcl:.2f} ml/min")