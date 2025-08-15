# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

# Program to print increasing star pattern
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print("*" * i ,end="")
    print("")
