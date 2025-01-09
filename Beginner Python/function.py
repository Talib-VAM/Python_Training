# Functions in Python
# Functions are reusable blocks of code designed to perform a specific task. They help in organizing code, improving readability, and avoiding repetition. Python functions are defined using the def keyword.

1.
# Function to calculate factorial of a number
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}.")

#output
# Enter a number: 5
# The factorial of 5 is 120.

2.
# Find Common Elements Between Two Lists

def common_elements(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(f"Common elements: {common_elements(list1, list2)}")

#output
# Common elements: [4, 5]

3.
# Build a Shopping Cart System

# Function to handle a shopping cart
def shopping_cart():
    cart = {}
    
    def add_item(item, quantity):
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"Added {quantity} {item}(s) to the cart.")

    def remove_item(item, quantity):
        if item in cart:
            if cart[item] > quantity:
                cart[item] -= quantity
                print(f"Removed {quantity} {item}(s) from the cart.")
            elif cart[item] == quantity:
                del cart[item]
                print(f"Removed {item} completely from the cart.")
            else:
                print(f"Error: You only have {cart[item]} {item}(s) in the cart.")
        else:
            print(f"Error: {item} is not in the cart.")

    def view_cart():
        if cart:
            print("Your shopping cart:")
            for item, quantity in cart.items():
                print(f" - {item}: {quantity}")
        else:
            print("Your cart is empty.")

    return add_item, remove_item, view_cart

add_item, remove_item, view_cart = shopping_cart()

add_item("Apple", 3)
add_item("Banana", 2)
view_cart()
remove_item("Apple", 1)
view_cart()
remove_item("Banana", 2)
view_cart()

#output
# Added 3 Apple(s) to the cart.
# Added 2 Banana(s) to the cart.
# Your shopping cart:
#  - Apple: 3
#  - Banana: 2
# Removed 1 Apple(s) from the cart.
# Your shopping cart:
#  - Apple: 2
#  - Banana: 2
# Removed Banana completely from the cart.
# Your cart is empty.
