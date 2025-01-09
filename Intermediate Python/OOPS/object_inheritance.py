# Object Inheritance in Python
# Inheritance allows one class (child class) to inherit attributes and methods from another class (parent class). This facilitates code reuse and extends the functionality of existing code

# 1. Simple Inheritance
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Child Class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

# Using the classes
dog = Dog("Buddy")
dog.eat()  # Inherited from the Animal class
dog.bark()  # Specific to Dog class


# Buddy is eating.
# Buddy says Woof!

# 2. Overriding Methods

# Parent Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

# Child Class
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Call the parent constructor
        self.department = department

    # Overriding the show_details method
    def show_details(self):
        print(f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}")

# Using the classes
emp = Employee("Alice", 50000)
mgr = Manager("Bob", 80000, "Sales")

emp.show_details()
mgr.show_details()

#output

# Employee: Alice, Salary: 50000
# Manager: Bob, Salary: 80000, Department: Sales


# Example 3: Multiple Inheritance

# Parent Class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Parent Class 2
class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def display_job(self):
        print(f"Employee ID: {self.employee_id}, Position: {self.position}")

# Child Class (inherits from both Person and Employee)
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, position)
        self.department = department

    def display_manager(self):
        self.display_info()  # From Person
        self.display_job()   # From Employee
        print(f"Department: {self.department}")

# Using the classes
mgr = Manager("Charlie", 35, "M123", "Manager", "IT")
mgr.display_manager()

#output
# Name: Charlie, Age: 35
# Employee ID: M123, Position: Manager
# Department: IT



