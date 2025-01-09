# While Loops in Python
# A while loop repeatedly executes a block of code as long as the specified condition evaluates to True. Proper control of the loop is essential to avoid infinite loops

1.
# Guess the Number Game

import random

target = random.randint(1, 10)  # Random number between 1 and 10
guess = 0

while guess != target:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("You guessed it!")

#output
# Guess a number between 1 and 10: 5
# Too low!
# Guess a number between 1 and 10: 8
# Too high!
# Guess a number between 1 and 10: 7
# You guessed it!

2.
# Calculate the Sum of Positive Numbers
# Sum positive numbers until a negative number is entered
total = 0

print("Enter positive numbers to sum them. Enter a negative number to stop.")
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break  # Exit the loop
    total += num

print(f"The total sum of positive numbers is: {total}")

#output
# Enter positive numbers to sum them. Enter a negative number to stop.
# Enter a number: 10
# Enter a number: 20
# Enter a number: -5
# The total sum of positive numbers is: 30

3.
# Simulate an ATM Withdrawal System

# ATM simulation
balance = 1000  # Initial balance

print("Welcome to the ATM!")
print("1. Check Balance")
print("2. Withdraw")
print("3. Deposit")
print("4. Exit")

while True:
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(f"Your balance is: ${balance}")
        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds.")
            elif amount <= 0:
                print("Invalid amount.")
            else:
                balance -= amount
                print(f"Withdrawal successful. New balance: ${balance}")
        elif choice == 3:
            amount = int(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("Invalid amount.")
            else:
                balance += amount
                print(f"Deposit successful. New balance: ${balance}")
        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break  # Exit the loop
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")

#output
# Welcome to the ATM!
# 1. Check Balance
# 2. Withdraw
# 3. Deposit
# 4. Exit
# Enter your choice: 1
# Your balance is: $1000
# Enter your choice: 2
# Enter the amount to withdraw: 500
# Withdrawal successful. New balance: $500
# Enter your choice: 4
# Thank you for using the ATM. Goodbye!
