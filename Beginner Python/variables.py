1. # Assigning values to multiple variables in a single line
x, y, z = 10, 20, "Python"

print(f"x: {x}, y: {y}, z: {z}")

# Output
# x: 10, y: 20, z: Python



2. # Swapping values between variables
a, b = 5, 10
a, b = b, a
print(f"a: {a}, b: {b}")

# Output
# a: 10, b: 5

3. # Nested data structure: A dictionary with lists and nested dictionaries
person = {
    "name": "Talib",
    "age": 30,
    "skills": ["Python", "Machine Learning", "Data Analysis"],
    "details": {
        "city": "New York",
        "job": "Data Scientist"
    }
}

# Accessing and modifying variables
person["skills"].append("Deep Learning")  # Add a skill
person["details"]["city"] = "India"  # Update city


print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"Skills: {', '.join(person['skills'])}")
print(f"Details: {person['details']}")

# Output

# Name: Talib
# Age: 30
# Skills: Python, Machine Learning, Data Analysis, Deep Learning
# Details: {'city': 'India', 'job': 'Data Scientist'}
