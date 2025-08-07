# 5. Label the program written in problem 4 with comments. 

# Ask the user how many terms they want in the Fibonacci series
n = int(input("Enter the number of terms: "))

# First two terms of the Fibonacci series
a = 0
b = 1

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("Fibonacci series up to 1 term:")
    print(a)
else:
    print("Fibonacci series:")
    print(a, b, end=" ")  # Print the first two terms

    # Loop to generate the next terms
    for _ in range(2, n):
        c = a + b      # Next term is the sum of the previous two
        print(c, end=" ")
        a = b          # Move one step forward
        b = c
