# 6. Write a program to calculate the factorial of a given number using for loop.
# 5 = 1 x 2 x 3 x 4 x 5

# Program to calculate factorial of a given number using for loop

num = int(input("Enter a number: "))

factorial = 1  # factorial starts at 1

for i in range(1, num + 1):
    factorial *= i  # multiply factorial by current number

print(f"The factorial of {num} is {factorial}")
