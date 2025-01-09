# Returning Values from Functions in Python
# In Python, functions can return values to the caller using the return statement. This allows a function to produce a result that can be used elsewhere in the program. The return statement can return a single value, multiple values (as a tuple), or even other functions.

1.
# Simple Return Value


def add(a, b):
    return a + b

# Calling the function and storing the result
result = add(5, 3)


print(f"The sum of 5 and 3 is {result}")

#output
# The sum of 5 and 3 is 8

2.
# Returning Multiple Values
# In this example, a function returns multiple values, which are captured as a tuple.


def get_student_info(name, age, grade):
    return name, age, grade  # Returning a tuple

# Calling the function and unpacking the returned tuple
name, age, grade = get_student_info("Alice", 20, "A")

# Printing the returned values
print(f"Name: {name}, Age: {age}, Grade: {grade}")

#output
# Name: Alice, Age: 20, Grade: A

3.
# Returning a Function (Higher-Order Function)
# A higher-order function is a function that either takes one or more functions as arguments or returns a function.

# Function that returns another function
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function  

# Calling outer_function and capturing the returned function
add_5 = outer_function(5)

# Using the returned function to add 5 to other numbers
print(add_5(10))  # 5 + 10 = 15
print(add_5(20))  # 5 + 20 = 25

#output15
25
20

