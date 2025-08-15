# 4. Write a program to find whether a given number is prime or not
n = int(input("Enter a number: "))
for i in range(2, n):
    if(n%i) == 0:
        print("Number is not primer")
        break
else:
    print("Number is prime")


"""
# Program to check whether a given number is prime or not

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number")
else:
    i = 2
    is_prime = True  # assume prime until proven otherwise

    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")


"""