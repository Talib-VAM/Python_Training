# Variable Naming Rules in Python
# 1. Must start with a letter (a-z, A-Z) or an underscore _.
# 2. Cannot start with a digit (0-9).
# 3. Can contain letters, digits, and underscores (_).
# 4. Case-sensitive: myVar and myvar are different variables.
# 5. Cannot use reserved keywords (e.g., if, else, while, class, etc.).
# 6. Should be meaningful and descriptive for better readability.


1 #Descriptive Variable Names

# Using descriptive names for variables
first_name = "Md Talib"
last_name = "Ansari"

# Combining variables into a full name
full_name = f"{first_name} {last_name}"
print(full_name) 
# Output: Md Talib Ansari

2. # Using Underscores for Readability

student_score = 95
max_score = 100

# Calculating percentage
percentage = (student_score / max_score) * 100
print(f"Percentage: {percentage}%") 
 # Output: Percentage: 95.0%



3. # Underscore naming for better readability
student_score = 95
max_score = 100

# Calculating percentage
percentage = (student_score / max_score) * 100
print(f"Percentage: {percentage}%") 
 # Output: Percentage: 95.0%



4. #Using Variables to Store a Nested Data Structure

employee_data = {
    "employee_id": 101,
    "employee_name": "Md Talib",
    "skills": ["Python", "Machine Learning", "Data Visualization"],
    "performance_scores": {
        "2022": 85,
        "2023": 90,
    }
}

# Accessing data using variable names
skills = employee_data["skills"]
performance_2023 = employee_data["performance_scores"]["2023"]


print(f"Skills: {', '.join(skills)}")
print(f"Performance Score (2023): {performance_2023}")

# Output

# Skills: Python, Machine Learning, Data Visualization
# Performance Score (2023): 90
