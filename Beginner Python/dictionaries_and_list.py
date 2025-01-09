# Python Dictionaries and Lists
# Dictionaries in Python are unordered collections of key-value pairs. Keys must be unique and immutable, while values can be any data type.
# Lists in Python are ordered collections of items, and the items can be of any data type. Lists are mutable, meaning their elements can be changed.

1.
# Working with Dictionaries

# Create a dictionary with student names and their scores
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95
}

# Accessing a value using a key
print(f"Alice's score: {student_scores['Alice']}")

# Adding a new key-value pair
student_scores["Eve"] = 88

# Looping through the dictionary
for student, score in student_scores.items():
    print(f"{student}: {score}")

#output
# Alice's score: 85
# Alice: 85
# Bob: 92
# Charlie: 78
# David: 95
# Eve: 88

2.
# Nested Lists

# Create a nested list (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in the nested list
print("Element at position (2, 1):", matrix[1][0])  # Row 2, Column 1
print("Element at position (0, 2):", matrix[0][2])  # Row 1, Column 3

# Looping through the nested list
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

#output
# Element at position (2, 1): 4
# Element at position (0, 2): 3
# 1 2 3 
# 4 5 6 
# 7 8 9

3.
# Merging Dictionaries and Lists

# Merging two dictionaries
dict1 = {"Alice": 85, "Bob": 92}
dict2 = {"Charlie": 78, "David": 95}

merged_dict = {**dict1, **dict2}  # Merging using unpacking
print("Merged Dictionary:", merged_dict)

# Merging a dictionary and a list of tuples (key-value pairs)
student_grades = [("Eve", 88), ("Frank", 91)]
for student, grade in student_grades:
    merged_dict[student] = grade

print("Updated Merged Dictionary:", merged_dict)

# List of dictionaries (e.g., student records)
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

# Adding a new student's record
students.append({"name": "David", "score": 95})

# Accessing each student's information
for student in students:
    print(f"Student: {student['name']}, Score: {student['score']}")

#output
# Merged Dictionary: {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
# Updated Merged Dictionary: {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88, 'Frank': 91}
# Student: Alice, Score: 85
# Student: Bob, Score: 92
# Student: Charlie, Score: 78
# Student: David, Score: 95

