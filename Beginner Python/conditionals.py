# Conditionals in Python: if, elif, else
# Conditionals are used to execute specific code blocks based on conditions. The structure typically follows:

# python
# Copy code
# if condition1:
#     # Block 1
# elif condition2:
#     # Block 2
# else:
#     # Block 3

1.
# Grading System

# Input a score and determine the grade
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")


# Output
# Enter your score: 85
# Your grade is: B

2.
# Checking Even or Odd with Additional Checks
# Input a number and check properties
number = int(input("Enter a number: "))

if number % 2 == 0:
    if number > 0:
        result = "Positive Even"
    elif number < 0:
        result = "Negative Even"
    else:
        result = "Zero (neither positive nor negative)"
else:
    if number > 0:
        result = "Positive Odd"
    else:
        result = "Negative Odd"


print(f"The number is: {result}")

# Output
# Enter a number: -7
# The number is: Negative Odd

3.
# Nested Conditions for Loan Approval

# Determine loan approval based on multiple conditions
income = int(input("Enter your monthly income: "))
credit_score = int(input("Enter your credit score: "))
existing_loans = int(input("Enter the number of existing loans: "))

if income >= 3000:
    if credit_score >= 700:
        if existing_loans == 0:
            decision = "Loan Approved"
        elif existing_loans <= 2:
            decision = "Loan Approved with Conditions"
        else:
            decision = "Loan Denied (Too many loans)"
    else:
        decision = "Loan Denied (Low credit score)"
else:
    decision = "Loan Denied (Low income)"


print(f"Decision: {decision}")

# Input/Output

# Enter your monthly income: 4000
# Enter your credit score: 750
# Enter the number of existing loans: 1
# Decision: Loan Approved with Conditions

