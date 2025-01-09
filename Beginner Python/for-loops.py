# For Loops in Python
# For loops in Python are used to iterate over sequences (like lists, tuples, strings, or ranges). They are useful for executing a block of code multiple times with varying conditions.

1.
# Calculate the sum of squares of numbers in a list
numbers = [1, 2, 3, 4, 5]
sum_of_squares = 0

for num in numbers:
    sum_of_squares += num ** 2

print(f"Sum of squares: {sum_of_squares}")

#output
# Sum of squares: 55

2.

# Find prime numbers within a given range
start = 10
end = 30
print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num > 1:  # Prime numbers are greater than 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

#output
# Prime numbers between 10 and 30:
# 11 13 17 19 23 29

3.
# Building a Multiplication Table

# Create a multiplication table using nested for loops
rows = 10
cols = 10

print("Multiplication Table:")
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(f"{i * j:4}", end=" ")  # Align columns for readability
    print()  # New line after each row

    #output
#     Multiplication Table:
#    1    2    3    4    5    6    7    8    9   10
#    2    4    6    8   10   12   14   16   18   20
#    3    6    9   12   15   18   21   24   27   30
#    4    8   12   16   20   24   28   32   36   40
#    5   10   15   20   25   30   35   40   45   50
#    6   12   18   24   30   36   42   48   54   60
#    7   14   21   28   35   42   49   56   63   70
#    8   16   24   32   40   48   56   64   72   80
#    9   18   27   36   45   54   63   72   81   90
#   10   20   30   40   50   60   70   80   90  100


