# 8. Write a python function to print multiplication table of a given number.
def multiplication_table(n):
    for i in range(1, 11):   # Table up to 10
        print(f"{n} x {i} = {n*i}")


n = int(input("Enter a number : "))
# Example usage
multiplication_table(n)

