# 4. Write a recursive function to calculate the sum of first n natural numbers.
'''
sun(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4 ..... (n-1) + n
sum(n) = sum(n-1)+n

'''

def sum_natural(n):
    # Base case: if n = 1, return 1
    if n == 1:
        return 1
    # Recursive case: n + sum of numbers up to n-1
    else:
        return n + sum_natural(n - 1)


# Example usage
n = 5
print("Sum of first", n, "natural numbers is:", sum_natural(n))
