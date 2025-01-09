# Logical Operators in Python
# Logical operators in Python are used to combine conditional statements:

# and: Returns True if both conditions are True.
# or: Returns True if at least one condition is True.
# not: Reverses the result; returns True if the condition is False.

1.
# Eligibility Check

# Check if a person is eligible for a membership
age = int(input("Enter your age: "))
income = int(input("Enter your monthly income: "))

if age >= 18 and income >= 3000:
    print("You are eligible for the membership.")
else:
    print("You are not eligible for the membership.")


# Input/Output
# Enter your age: 20
# Enter your monthly income: 4000
# You are eligible for the membership.

2.
# Login System

# Simulate a login system
username = input("Enter username: ")
password = input("Enter password: ")

if (username == "admin" and password == "password123") or (username == "guest" and password == "guest123"):
    print("Login successful!")
else:
    print("Login failed!")

#Input/Output

# Enter username: admin
# Enter password: password123
# Login successful!

3.
# Complex Admission Criteria

# Admission based on multiple criteria
grades = float(input("Enter your average grades (out of 10): "))
entrance_score = int(input("Enter your entrance exam score (out of 100): "))
extra_curricular = input("Are you involved in extracurricular activities? (yes/no): ").lower()

if (grades >= 8.0 and entrance_score >= 75) or (grades >= 7.0 and entrance_score >= 60 and extra_curricular == "yes"):
    print("Admission Granted")
else:
    print("Admission Denied")

# Input/Output
# Enter your average grades (out of 10): 8.5
# Enter your entrance exam score (out of 100): 80
# Are you involved in extracurricular activities? (yes/no): no
# Admission Granted


