# Data Types in Python
# Python provides several built-in data types to work with different kinds of data. These can be broadly categorized into:

# Numeric Types
# Sequence Types
# Mapping Type
# Set Types
# Boolean Type
# None Type

# 1. Numeric Types
# int: Integer values.
# float: Decimal (floating-point) numbers.
# complex: Complex numbers (3+4j).

# Numeric types
x = 10         # int
y = 3.14       # float
z = 2 + 3j     # complex

print(f"x is {type(x)}, y is {type(y)}, z is {type(z)}")

#output

# x is <class 'int'>, y is <class 'float'>, z is <class 'complex'>

2. #Sequence Types
# str: A sequence of characters (strings).
# list: An ordered, mutable collection of elements.
# tuple: An ordered, immutable collection of elements.

# Sequence types
string = "Python"       # str
my_list = [1, 2, 3]     # list
my_tuple = (4, 5, 6)    # tuple

print(f"string: {type(string)}, list: {type(my_list)}, tuple: {type(my_tuple)}")

#output
# string: <class 'str'>, list: <class 'list'>, tuple: <class 'tuple'>


# 3. Mapping Type
# dict: A collection of key-value pairs.

# Dictionary
my_dict = {"name": "Alice", "age": 30}

print(f"my_dict: {type(my_dict)}")
print(f"Name: {my_dict['name']}, Age: {my_dict['age']}")


#output
# my_dict: <class 'dict'>
# Name: Alice, Age: 30

4. # Set Types
# set: An unordered collection of unique elements.
# frozenset: An immutable version of a set.

# Set and frozenset
my_set = {1, 2, 3, 3}       # Duplicate 3 will be removed
my_frozenset = frozenset(my_set)

print(f"my_set: {my_set}, type: {type(my_set)}")
print(f"my_frozenset: {my_frozenset}, type: {type(my_frozenset)}")

#output
# my_set: {1, 2, 3}, type: <class 'set'>
# my_frozenset: frozenset({1, 2, 3}), type: <class 'frozenset'>


5.  
# Boolean Type
# bool: Represents True or False.

is_valid = True
is_empty = False

print(f"is_valid: {type(is_valid)}, is_empty: {type(is_empty)}")

#output
# is_valid: <class 'bool'>, is_empty: <class 'bool'>

6.
# None Type
# NoneType: Represents the absence of a value (or a null value).

value = None
print(f"value: {value}, type: {type(value)}")

#output
# value: None, type: <class 'NoneType'>


# Dynamic Typing in Python
# Python is dynamically typed, meaning you don’t have to declare the type of a variable explicitly. It is inferred during runtime.

x = 42          # Initially an integer
x = "Hello"     # Now a string
print(f"x: {x}, type: {type(x)}")

# x: Hello, type: <class 'str'>




# Category	Type	Example
# Numeric	int	10
# Numeric	float	3.14
# Numeric	complex	1+2j
# Sequence	str	"Hello"
# Sequence	list	[1, 2, 3]
# Sequence	tuple	(4, 5, 6)
# Mapping	dict	{"key": "value"}
# Set	set	{1, 2, 3}
# Set	frozenset	frozenset({1, 2, 3})
# Boolean	bool	True, False
# None Type	NoneType	None