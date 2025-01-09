1.# Using String Slicing
# String slicing to extract specific parts of a string
text = "Python Programming"

# Extracting a substring
substring = text[7:18]

# Reversing the string
reversed_text = text[::-1]


print(f"Substring: {substring}")
print(f"Reversed: {reversed_text}")

# Output
# Substring: Programming
# Reversed: gnimmargorP nohtyP


2.# String Formatting with f-strings

# Using f-strings for formatted output
name = "Talib"
age = 30
city = "India"

# Formatted string
formatted_string = f"My name is {name}, I am {age} years old, and I live in {city}."

print(formatted_string)

# Output
# My name is Talib, I am 30 years old, and I live in New York.


3.#Complex String Manipulation with Regular Expressions

import re

# Sample string
text = "Email me at talib@gmail.com or bob123@company.org for details."

# Extract all email addresses using regular expressions
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Replace email addresses with [hidden]
redacted_text = re.sub(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", "[hidden]", text)

print(f"Extracted Emails: {emails}")
print(f"Redacted Text: {redacted_text}")

# Output
# Extracted Emails: ['talib@gmail.com', 'bob123@company.org']
# Redacted Text: Email me at [hidden] or [hidden] for details.


