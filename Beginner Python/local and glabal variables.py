# Scope and Local/Global Variables in Python
# In Python, scope refers to the region of the program where a variable can be accessed or modified. Variables can either be local or global, and their accessibility depends on where they are defined.

# Local Variables: These are variables defined inside a function or block and can only be used within that function or block.
# Global Variables: These are variables defined outside any function or block, typically at the top level of the program, and can be accessed from anywhere within the program.

# 1: Local Variables
# Local variables are defined within a function and are not accessible outside the function.

# Function to demonstrate local variable scope
def calculate_area(length, width):
    area = length * width  # Local variable
    print(f"Area inside function: {area}")

# Call the function
calculate_area(5, 10)

# Trying to access the local variable outside the function will cause an error
# print(area)  # This will raise a NameError because 'area' is local to the function

#output
# Area inside function: 50

# 2: Global Variables
# Global variables are defined outside any function and can be accessed from anywhere in the program.

# Global variable
global_variable = 100

# Function that accesses the global variable
def print_global_variable():
    print(f"Global variable inside function: {global_variable}")

# Call the function
print_global_variable()

# Accessing the global variable outside the function
print(f"Global variable outside function: {global_variable}")


#output

# Global variable inside function: 100
# Global variable outside function: 100


3.

# 3: Modifying Global Variables Inside a Function

# Global variable
counter = 0

# Function to modify the global variable
def increment_counter():
    global counter  # Using the global keyword to modify the global variable
    counter += 1  # Increment the global counter

# Calling the function multiple times
increment_counter()
increment_counter()

# Accessing the modified global variable
print(f"Modified global counter: {counter}")

#output

# Modified global counter: 2
