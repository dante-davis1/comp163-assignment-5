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
