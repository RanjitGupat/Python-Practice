# 4. Write a program to filter a list of numbers which are divisible by 5.


def divisible5(n):
    if(n%5==0):
        return True
    return False

a = [1, 2, 343, 45654, 1230, 4658, 67, 48765, 98, 50]

f = list(filter(divisible5,a))
print(f)