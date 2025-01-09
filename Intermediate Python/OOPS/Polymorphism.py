class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Function demonstrating polymorphism
def print_area(shape):
    print(f"Area: {shape.area()}")

# Create objects
rect = Rectangle(10, 5)
circle = Circle(7)

# Call the function with different shapes
print_area(rect)
print_area(circle)

#Output
Area: 50
Area: 153.86
