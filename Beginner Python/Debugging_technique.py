# Debugging Techniques in Python
# Debugging is the process of identifying and fixing issues (bugs) in your code. Python provides several ways to debug your code, from simple print statements to more advanced debugging tools.

# 1: Using Print Statements
# Print statements are the simplest and most commonly used debugging technique. You can insert print() statements in your code to check the values of variables or the flow of execution.

def calculate_area(length, width):
    # Debugging with print statements
    print(f"Length: {length}, Width: {width}")
    
    area = length * width
    print(f"Area: {area}")  # Print area value to debug
    
    return area

# Call the function and see the output
area = calculate_area(5, 10)

#output
# Length: 5, Width: 10
# Area: 50

2.
# Using Assertions
# Assertions are used to check whether a certain condition is True. If the condition is False, an AssertionError is raised, which can help catch errors early in the program.

def divide(a, b):
    # Assert that the divisor is not zero
    assert b != 0, "Error: Division by zero"
    return a / b

# Test the function with different values
print(divide(10, 2))  # This will work
print(divide(10, 0))  # This will raise an AssertionError

# 5.0
# AssertionError: Error: Division by zero

# 3: Using the Python Debugger (pdb)

# The Python Debugger (pdb) is a powerful tool for interactive debugging. It allows you to pause the program's execution and step through the code line by line, inspect variable values, and modify them if necessary.

import pdb

def factorial(n):
    pdb.set_trace()  # Start the debugger at this point
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Call the function
result = factorial(5)
print(f"Factorial: {result}")

#output

# > <filename>(5)<module>()
# -> if n == 0:
# (Pdb)

