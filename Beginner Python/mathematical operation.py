1. #Using Modulus and Floor Division
# Calculate quotient and remainder
dividend = 47
divisor = 6

quotient = dividend // divisor  # Floor division
remainder = dividend % divisor  # Modulus


print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")

# Output

Quotient: 7
Remainder: 5


2. # Calculating power and square root
base = 5
exponent = 3
square_root_of_base = base ** 0.5  # Square root using exponentiation


print(f"{base} raised to the power {exponent} is {base ** exponent}")
print(f"Square root of {base} is {square_root_of_base:.2f}")

# Output

# 5 raised to the power 3 is 125
# Square root of 5 is 2.24


# 3. Solving a Quadratic Equation


import math

# Coefficients of the quadratic equation
a = 1
b = -7
c = 10

# Calculate the discriminant
discriminant = b**2 - 4*a*c

if discriminant >= 0:
    # Calculate the two solutions
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The roots of the equation are {root1:.2f} and {root2:.2f}")
else:
    print("No real roots exist.")

#output
# The roots of the equation are 5.00 and 2.00
