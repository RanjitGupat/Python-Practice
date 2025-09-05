# 5. Write a program to find the maximum of the numbers in a list using the reduce
# function.
from functools import reduce

a = [190, 22, 343, 45654, 1230, 4658, 67, 48765, 98, 50]
def greater(a, b):
    if a > b:
        return a
    return b

print(reduce(greater, a))
