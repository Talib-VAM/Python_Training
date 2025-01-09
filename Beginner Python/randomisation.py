# Randomization in Python
# Python provides the random module to perform randomization tasks such as generating random numbers, selecting random elements, shuffling, etc.

1.
# Rolling a Pair of Dice

import random

# Simulate rolling two dice
die1 = random.randint(1, 6)  # Random integer between 1 and 6
die2 = random.randint(1, 6)

print(f"Dice rolls: {die1}, {die2}")
print(f"Total: {die1 + die2}")

#output
# Dice rolls: 3, 5
# Total: 8

2.
# Random Password Generator

import random
import string

# Generate a random password
length = 10
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(characters, k=length))

print(f"Generated password: {password}")

#output
# Generated password: Gt$5pA1@wZ

3.
# Simulating a Lottery System

import random

# Define the pool of participants
participants = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"]

# Randomly select a winner
winner = random.choice(participants)

# Randomly select 3 consolation prize winners (without duplicates)
consolation_winners = random.sample(participants, 3)

# Remove the winner from the consolation list if they are chosen
if winner in consolation_winners:
    consolation_winners.remove(winner)

print(f"Grand Prize Winner: {winner}")
print(f"Consolation Prize Winners: {consolation_winners}")
#output
# Grand Prize Winner: Charlie
# Consolation Prize Winners: ['Grace', 'Eve', 'David']

