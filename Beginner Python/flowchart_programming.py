# Flowcharts and Programming
# Flowcharts are visual representations of the flow of a program or algorithm. They use standardized symbols to represent actions, decisions, or inputs/outputs, making it easier to understand the logic and flow of a program.

1.
# Calculate Factorial
# Problem: Create a flowchart and Python code to calculate the factorial of a given number.

# Flowchart Steps:

# Start.
# Input a number, n.
# Initialize factorial = 1.
# Check if i <= n.
# If Yes, multiply factorial by i and increment i.
# If No, go to Step 5.
# Print factorial.
# End.

n = int(input("Enter a number to calculate its factorial: "))
factorial = 1

i = 1
while i <= n:
    factorial *= i
    i += 1

print(f"The factorial of {n} is {factorial}.")


2.
# Check If a Number is Prime
# Problem: Create a flowchart and Python code to check if a number is prime.

# Flowchart Steps:

# Start.
# Input a number, n.
# If n <= 1, print "Not Prime" and end.
# Initialize i = 2.
# Check if i <= sqrt(n).
# If n % i == 0, print "Not Prime" and end.
# Otherwise, increment i.
# If no divisors are found, print "Prime".
# End.

import math

n = int(input("Enter a number to check if it's prime: "))

if n <= 1:
    print("Not Prime")
else:
    is_prime = True
    i = 2
    while i <= math.isqrt(n):
        if n % i == 0:
            is_prime = False
            break
        i += 1
    
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

3.
# ATM Transaction System
# Problem: Create a flowchart and Python code to simulate an ATM system with the following features:

# Check balance.
# Withdraw money.
# Deposit money.
# Exit the system.
# Flowchart Steps:

# Start.
# Display menu:
# 1: Check Balance.
# 2: Withdraw.
# 3: Deposit.
# 4: Exit.
# Input user choice.
# Based on the choice:
# If 1, display the balance and go back to Step 2.
# If 2, input withdrawal amount. If sufficient balance, deduct amount; otherwise, show an error and go back to Step 2.
# If 3, input deposit amount, add it to the balance, and go back to Step 2.
# If 4, exit.
# End.

# ATM Simulation
balance = 1000

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print(f"Your current balance is: ${balance}")
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            balance -= amount
            print(f"Withdrawal successful. New balance: ${balance}")
    elif choice == 3:
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount.")
        else:
            balance += amount
            print(f"Deposit successful. New balance: ${balance}")
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

