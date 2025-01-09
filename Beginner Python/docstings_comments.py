# Docstrings vs Comments in Python
# In Python, docstrings and comments are both used to document code, but they have different purposes and usage.

# Docstrings: Used to describe the purpose of a function, class, or module. They are written in triple quotes and can be accessed using help() or .__doc__ attributes. They are formal documentation meant to explain the functionality of the code to others or for generating documentation automatically.

# Comments: Used to explain or annotate the code, typically for developers or to clarify why certain code exists. They are written using # and are ignored by Python when the code runs.

# 1: Using Comments

# This is a comment explaining the following line of code
x = 10  # Assigning 10 to variable x

# This function calculates the square of a number
def square(num):
    # Multiply the number by itself
    return num * num

result = square(5)  # Call the function and store the result
print(result)  # Output the result

2.
# 2: Using Docstrings

# Function to calculate the square of a number
def square(num):
    """
    This function takes a number as input and returns its square.
    
    Arguments:
    num -- a number to be squared
    
    Returns:
    The square of the number.
    """
    return num * num

# Accessing the docstring of the square function
print(square.__doc__)  # Prints the docstring for the square function

#output
    # This function takes a number as input and returns its square.
    
    # Arguments:
    # num -- a number to be squared
    
    # Returns:
    # The square of the number.

3.
# Combining Comments and Docstrings

# This function calculates the area of a rectangle.
def rectangle_area(length, width):
    """
    This function calculates the area of a rectangle given its length and width.
    
    Arguments:
    length -- the length of the rectangle
    width -- the width of the rectangle
    
    Returns:
    The area of the rectangle.
    """
    # Check if the inputs are valid
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers")
    
    # Return the area of the rectangle
    return length * width

# Call the function and print the area
try:
    area = rectangle_area(5, 10)
    print(f"Area of rectangle: {area}")
except ValueError as e:
    print(e)

#output

# Area of rectangle: 50

