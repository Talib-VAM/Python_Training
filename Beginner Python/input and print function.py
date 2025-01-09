1. #Using Input to Calculate and Print Results

# Input numbers and calculate their sum
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate sum
total = num1 + num2

print(f"The sum of {num1} and {num2} is {total}.")

# output
# Enter the first number: 5
# Enter the second number: 10
# The sum of 5 and 10 is 15.

2. #Handling Multiple Inputs in a Single Line

name, age, city = input("Enter your name, age, and city separated by commas: ").split(", ")

print(f"Name: {name}\nAge: {age}\nCity: {city}")

#output
# Enter your name, age, and city separated by commas: Talib, 30, India
# Name: Talib
# Age: 30
# City: India

3. #Dynamic Table Printing with User Input

# Input: number of rows and columns
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Create a dynamic table
print("\nDynamic Table:")
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print(f"{i * j:4}", end=" ")
    print()  # New line after each row

#ouput 
# Output (Input: 3 rows, 5 columns):
# Enter the number of rows: 3
# Enter the number of columns: 5

# Dynamic Table:
#    1    2    3    4    5 
#    2    4    6    8   10 
#    3    6    9   12   15


