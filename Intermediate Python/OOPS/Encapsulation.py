class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Setter for balance
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount! Balance cannot be negative.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount!")

# Create an object
account = BankAccount("123456", 5000)

# Access balance using getter
print("Initial Balance:", account.get_balance())

# Modify balance using setter
account.set_balance(6000)
print("Updated Balance:", account.get_balance())

# Deposit money
account.deposit(1000)
print("Final Balance:", account.get_balance())
