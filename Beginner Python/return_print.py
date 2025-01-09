# Difference Between return and print in Python
# The **return** statement is used to send a result from a function back to the caller. It allows the function to produce a result that can be stored or used in further operations.
# The **print** function is used to output data to the console, primarily for displaying information to the user or for debugging purposes. It does not send the result back to the caller.

# 1: Using return to Send Data Back

# Function to calculate the square of a number
def square(num):
    return num * num  # Returning the result

# Calling the function and storing the result
result = square(4)

# Printing the result outside the function
print(f"The square of 4 is {result}")

#output
# The square of 4 is 16

# 2: Using print to Display Data

# Function to calculate the square of a number and print the result
def square(num):
    print(f"The square of {num} is {num * num}")  # Printing the result directly

# Calling the function 
square(4)

#output
# The square of 4 is 16

3.
# Returning and Printing Values from Different Functions

# Function to multiply two numbers
def multiply(a, b):
    return a * b  

def area(length, width):
    area = length * width
    print(f"The area of the rectangle is {area}")  # Printing the result

# Using the multiply function to get the area
result = multiply(5, 10)

# Using the area function to print the area directly
area(5, 10)

# Printing the result stored in 'result'
print(f"The area calculated using the multiply function is {result}")

#output
# The area of the rectangle is 50
# The area calculated using the multiply function is 50

