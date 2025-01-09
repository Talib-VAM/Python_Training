class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass  # Abstract method (to be implemented by subclasses)

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Create objects
dog = Dog("Buddy")
cat = Cat("Kitty")

print(f"{dog.name} says: {dog.sound()}")
print(f"{cat.name} says: {cat.sound()}")
