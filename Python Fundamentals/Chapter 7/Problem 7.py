# 7. Write a program to print the following star pattern.
#  *
# ***
# ***** for n = 3

# Program to print star pattern
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" "* (n-i), end = "")
    # For each row, print (2*i - 1) stars
    print("*" * (2 * i - 1), end = "")
    print("")

