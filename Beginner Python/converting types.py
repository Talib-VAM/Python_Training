# Type Conversion in Python
# Python provides built-in functions for converting data types explicitly. These are also called type casting functions. Commonly used type conversion functions include:

# int(): Converts to an integer.
# float(): Converts to a floating-point number.
# str(): Converts to a string.
# list(), tuple(), set(): Converts to respective collection types.
# dict(): Converts to a dictionary (from suitable data formats).

1.
# Converting Between Strings and Numbers

# Convert string to integer and float
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)

# Convert back to string
new_str = str(num_int)

print(f"Integer: {num_int}, Float: {num_float}, String: '{new_str}'")

#output
# Integer: 123, Float: 123.0, String: '123'


2. 
# Convert a list to a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

# Convert back to a list and modify
modified_list = list(my_tuple)
modified_list.append(5)

print(f"Original List: {my_list}")
print(f"Converted Tuple: {my_tuple}")
print(f"Modified List: {modified_list}")

#output
# Original List: [1, 2, 3, 4]
# Converted Tuple: (1, 2, 3, 4)
# Modified List: [1, 2, 3, 4, 5]

3.
# Parsing and Converting Complex Data

# In this example, a string representing a JSON-like structure is parsed and converted into different Python types.

import json

# JSON-like string
data_str = '{"name": "Alice", "age": "30", "skills": "[Python, ML, AI]"}'

# Convert string to a dictionary
data_dict = json.loads(data_str)

# Convert specific fields to appropriate types
data_dict['age'] = int(data_dict['age'])  # Convert age to int
data_dict['skills'] = eval(data_dict['skills'])  # Convert skills to a list

print(f"Dictionary: {data_dict}")
print(f"Name: {data_dict['name']}, Age: {data_dict['age']}, Skills: {data_dict['skills']}")

#output
# Dictionary: {'name': 'Alice', 'age': 30, 'skills': ['Python', 'ML', 'AI']}
# Name: Alice, Age: 30, Skills: ['Python', 'ML', 'AI']

# JSON Parsing: The json.loads() function converts a JSON-like string into a Python dictionary.
# Type Conversions:
# int() converts the "age" field from a string to an integer.
# eval() is used to safely evaluate the "skills" string into a Python list.
# Dynamic Type Manipulation: Converting nested or structured data fields to their proper Python types is a common task in data processing.


