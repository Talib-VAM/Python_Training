# Creating Classes in Python
# Classes are blueprints for creating objects. They define attributes (data) and methods (functions) to work with those attributes. Below are two intermediate and one advanced example of creating classes in Python.

# 1: Creating a Class with Methods and Constructor

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Grade as a percentage

    def get_grade(self):
        return f"{self.name} has a grade of {self.grade}%."

# Using the class
student = Student("Alice", 20, 85)
print(student.get_grade())

#output
# Alice has a grade of 85%.

# 2. Class with Methods to Modify Attributes

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Available balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")

# Using the class
account = BankAccount("John Doe", 500)
account.deposit(200)
account.withdraw(100)
account.withdraw(700)

#output
# $200 deposited. New balance: $700
# $100 withdrawn. New balance: $600
# Insufficient funds! Available balance: $600

# 3: Class with Inheritance and Method Overriding

# Base Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"

# Subclass
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    # Overriding the show_details method
    def show_details(self):
        return f"Manager: {self.name}, Salary: ${self.salary}, Department: {self.department}"

# Subclass
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def show_details(self):
        return f"Developer: {self.name}, Salary: ${self.salary}, Programming Language: {self.programming_language}"

# Using the classes
manager = Manager("Sarah", 90000, "HR")
developer = Developer("Mike", 80000, "Python")

print(manager.show_details())
print(developer.show_details())

#output

# Manager: Sarah, Salary: $90000, Department: HR
# Developer: Mike, Salary: $80000, Programming Language: Python

