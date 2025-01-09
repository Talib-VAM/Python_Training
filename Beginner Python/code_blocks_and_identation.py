# Code Blocks and Indentation in Python
# Python uses indentation to define code blocks, instead of braces {} as in other languages. Proper indentation is critical, as it determines the structure and flow of a program.

1.
# Print a right-angled triangle pattern
rows = 5

for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(i):  # Inner loop for columns
        print("*", end=" ")
    print()  # New line after each row

#output
# *
# * *
# * * *
# * * * *
# * * * * *

2.
# Conditional Statement with Proper Indentation

# Check if a number is positive, negative, or zero
number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print("The number is zero.")

#output
# Enter a number: 10
# 10 is positive.

3.
# Indentation in a Function with Multiple Constructs

# Student Grade Analysis
def grade_analysis(scores):
    for student, score in scores.items():
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
        
        print(f"Student: {student}, Score: {score}, Grade: {grade}")


students_scores = {
    "Alice": 95,
    "Bob": 82,
    "Charlie": 67,
    "David": 50,
    "Eve": 74,
}
grade_analysis(students_scores)

#output
# Student: Alice, Score: 95, Grade: A
# Student: Bob, Score: 82, Grade: B
# Student: Charlie, Score: 67, Grade: D
# Student: David, Score: 50, Grade: F
# Student: Eve, Score: 74, Grade: C

