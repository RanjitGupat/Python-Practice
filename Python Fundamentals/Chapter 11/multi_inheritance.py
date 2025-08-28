class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)   #prints the a attributr
#print(o.b)   #Shows an error as there is no b attribute in employee  class

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)