# Nested Collections in Python
# Nested collections refer to data structures (lists, dictionaries, tuples) that contain other collections as their elements. This allows the organization of more complex data, where one collection can hold multiple other collections, making the data hierarchical.

1.
# Nested Lists
# A list can contain other lists, allowing you to store data in a matrix-like structure.

# Create a nested list (2D list)
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print("Element at (1, 1):", nested_list[1][1])  # Accessing the second row, second column
print("Element at (0, 2):", nested_list[0][2])  # Accessing the first row, third column

# Looping through the nested list to print all elements
for row in nested_list:
    for item in row:
        print(item, end=" ")
    print()

#output
# Element at (1, 1): 5
# Element at (0, 2): 3
# 1 2 3 
# 4 5 6 
# 7 8 9

2.
# Nested Dictionaries

# A dictionary can contain other dictionaries, which is useful for representing structured data, such as student records.

# Create a nested dictionary to represent student grades
students = {
    "Alice": {"Math": 85, "Science": 92, "English": 88},
    "Bob": {"Math": 78, "Science": 84, "English": 80},
    "Charlie": {"Math": 90, "Science": 91, "English": 94}
}

# Accessing nested dictionary values
print("Alice's Math grade:", students["Alice"]["Math"])
print("Charlie's Science grade:", students["Charlie"]["Science"])

# Looping through the dictionary to print all student grades
for student, subjects in students.items():
    print(f"\n{student}'s Grades:")
    for subject, grade in subjects.items():
        print(f"{subject}: {grade}")

        #output
#         Alice's Math grade: 85
# Charlie's Science grade: 91

# Alice's Grades:
# Math: 85
# Science: 92
# English: 88

# Bob's Grades:
# Math: 78
# Science: 84
# English: 80

# Charlie's Grades:
# Math: 90
# Science: 91
# English: 94


3.
# Nested Collections (Lists of Dictionaries)
# This example uses a list of dictionaries, where each dictionary represents a record (such as a student) with various attributes (e.g., name, age, grades).

# List of dictionaries representing student records
students = [
    {"name": "Alice", "age": 20, "grades": {"Math": 85, "Science": 92}},
    {"name": "Bob", "age": 22, "grades": {"Math": 78, "Science": 84}},
    {"name": "Charlie", "age": 21, "grades": {"Math": 90, "Science": 91}},
]

# Accessing and manipulating data in nested collections
for student in students:
    print(f"\nStudent: {student['name']}, Age: {student['age']}")
    for subject, grade in student["grades"].items():
        print(f"{subject}: {grade}")
    
    # Update a grade (e.g., Charlie's Science grade)
    if student["name"] == "Charlie":
        student["grades"]["Science"] = 95
        print("\nUpdated grades for Charlie:", student["grades"])

# Printing the updated list of students
print("\nUpdated Student Records:")
for student in students:
    print(student)

#output

# Student: Alice, Age: 20
# Math: 85
# Science: 92

# Student: Bob, Age: 22
# Math: 78
# Science: 84

# Student: Charlie, Age: 21
# Math: 90
# Science: 91

# Updated grades for Charlie: {'Math': 90, 'Science': 95}

# Updated Student Records:
# {'name': 'Alice', 'age': 20, 'grades': {'Math': 85, 'Science': 92}}
# {'name': 'Bob', 'age': 22, 'grades': {'Math': 78, 'Science': 84}}
# {'name': 'Charlie', 'age': 21, 'grades': {'Math': 90, 'Science': 95}}



