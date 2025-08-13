# 1. Write a program to find the greatest of four numbers entered by the user.

# Taking 4 numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if(a>b and a>c and a>d):
    print("Gretest number is : ",a)
elif(b>a and b>c and b>d):
    print("Gretest number is : ",b)
elif(c>a and c>b and c>d):
    print("Gretest number is : ",c)
elif(d>a and d>c and d>b):
    print("Gretest number is : ",d)