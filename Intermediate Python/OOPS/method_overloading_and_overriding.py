# Method Overloading and Overriding
# Overloading: Defining multiple methods with the same name but different parameters (simulated using default arguments in Python).
# Overriding: Redefining a method in a subclass.

class Calculator:
    # Method overloading using default arguments
    def add(self, a, b=0, c=0):
        return a + b + c

class AdvancedCalculator(Calculator):
    # Method overriding
    def add(self, a, b=0, c=0):
        print(f"Adding {a}, {b}, and {c}")
        return super().add(a, b, c)

# Create objects
basic_calc = Calculator()
adv_calc = AdvancedCalculator()

# Method overloading
print("Basic Calculator Result:", basic_calc.add(10, 20))  # Two arguments
print("Basic Calculator Result:", basic_calc.add(10, 20, 30))  # Three arguments

# Method overriding
print("Advanced Calculator Result:", adv_calc.add(10, 20, 30))  # Overridden method

#outPut
# Basic Calculator Result: 30
# Basic Calculator Result: 60
# Adding 10, 20, and 30
# Advanced Calculator Result: 60
