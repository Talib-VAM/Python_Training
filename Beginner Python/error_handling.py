# Error Handling in Python
# Error handling in Python is done using try, except, else, and finally blocks. It ensures that a program can handle unexpected situations gracefully instead of crashing.

1.
# Handling Division by Zero

# Division with error handling
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")
else:
    print(f"Result: {result}")
#output
# Enter the numerator: 10
# Enter the denominator: 0
# Error: Division by zero is not allowed.

2.
# File Reading with Error Handling

try:
    file_name = input("Enter the file name: ")
    with open(file_name, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to access '{file_name}'.")
else:
    print("File content:")
    print(content)

#output
# Enter the file name: example.txt
# Error: The file 'example.txt' does not exist.

3.
# Custom Error Handling in a Banking System

# Custom exceptions
class InsufficientFundsError(Exception):
    pass

# Simulate a banking system
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise InsufficientFundsError("Insufficient funds for this transaction.")
            elif amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")
            else:
                self.balance -= amount
                print(f"Withdrawal successful. New balance: ${self.balance}")
        except InsufficientFundsError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")


account = BankAccount(1000)

# Simulate transactions
account.withdraw(1500)  # Insufficient funds
account.withdraw(-50)   # Invalid amount
account.withdraw(500)   # Valid transaction

#output
# Error: Insufficient funds for this transaction.
# Error: Withdrawal amount must be greater than zero.
# Withdrawal successful. New balance: $500

