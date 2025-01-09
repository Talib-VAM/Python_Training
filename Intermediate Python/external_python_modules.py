# 1: Using the math Module
# The math module provides mathematical functions like trigonometric calculations, logarithms, and constants.

import math

# Calculate square root and power
number = 16
sqrt = math.sqrt(number)
power = math.pow(2, 3)

# Calculate sine of an angle (in radians)
angle = math.radians(30)  # Convert degrees to radians
sine = math.sin(angle)

print(f"Square root of {number}: {sqrt}")
print(f"2 raised to the power 3: {power}")
print(f"Sine of 30 degrees: {sine}")

#output

# Square root of 16: 4.0
# 2 raised to the power 3: 8.0
# Sine of 30 degrees: 0.49999999999999994
