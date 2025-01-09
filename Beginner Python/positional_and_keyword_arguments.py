# Positional and Keyword Arguments in Python
# In Python, functions can accept positional arguments and keyword arguments.

# Positional arguments are assigned to parameters based on their position.
# Keyword arguments are passed with the parameter name explicitly and are used when calling a function.

1.
# Using Positional Arguments

# Function to greet a person
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Calling the function with positional arguments
greet("Alice", 25)
greet("Bob", 30)

#output
# Hello, Alice! You are 25 years old.
# Hello, Bob! You are 30 years old.

2.
# Using Keyword Arguments

# Function to calculate area of a rectangle
def area(length, width):
    return length * width

# Calling the function with keyword arguments
print(area(length=5, width=3))
print(area(width=7, length=4)) 

#output
15
28


3.
# Using Both Positional and Keyword Arguments

# Function to create a greeting message
def create_message(greeting, name, punctuation="."):
    return f"{greeting}, {name}{punctuation}"

# Using positional and keyword arguments together
print(create_message("Hello", "Alice", punctuation="!"))  # Positional and Keyword Argument
print(create_message("Hi", "Bob"))  # Using default value for punctuation


#output
# Hello, Alice!
# Hi, Bob.
