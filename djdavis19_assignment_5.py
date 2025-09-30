# gicomp163-assignment-5
# Assignment 5 - Loops Practice
# This file contains three challenges: Collatz sequence, Prime checker, and Multiplication Table

# ----------------------------
# Challenge 1: Collatz sequence
# ----------------------------

current_number = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", end=" ")
while current_number != 1:
    print(current_number, end=" ")
    if current_number % 2 == 0:  # even
        current_number = current_number // 2
    else:  # odd
        current_number = 3 * current_number + 1
    step_count += 1
print(1)  # print the last 1 in the sequence
print("Steps:", step_count)

# Critical Thinking:
# A while loop is used here because we don't know how many iterations are needed.
# The loop continues until n becomes 1, which could take an unpredictable number of steps.

# Challenge 2: Prime Number Checker

n = int(input("\nEnter a number greater than 1: "))
print(f"Testing divisors from 2 to {n-1}...")

is_prime = True  # Assume prime unless we find divisor

for divisor in range(2, n):  # For loop because range is known
    if n % divisor == 0:
        print(f"{n} is not prime (divisible by {divisor})")
        is_prime = False
        break

if is_prime:
    print(f"{n} is prime!")

# Challenge 3: Multiplication Table Grid
# -------------------------------

print("\nMultiplication Table:")

# Header row
print("    ", end="")
for col in range(1, 11):
    print(f"{col:4}", end="")
print()

# Rows
for row in range(1, 11):  # Outer loop for rows
    print(f"{row:2} ", end="")  # Row label
    for col in range(1, 11):   # Inner loop for columns
        product = row * col
        print(f"{product:4}", end="")  # Format for alignment
    print()  # New line after each row