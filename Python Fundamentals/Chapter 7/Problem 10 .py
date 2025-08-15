# 10. Write a program to print multiplication table of n using for loops in reversed
# order

# Program to print multiplication table in reverse order

n = int(input("Enter a number: "))

print(f"\nMultiplication Table of {n} in Reverse Order:")
for i in range(10, 0, -1):  # start from 10, go down to 1
    print(f"{n} x {i} = {n * i}")
