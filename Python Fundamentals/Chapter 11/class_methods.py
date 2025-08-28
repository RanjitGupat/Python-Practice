# CLASS METHOD
# A class method is a method which is bound to the class and not the object of the class.
# @classmethod decorator is used to create a class method.


class Employee:
    a = 1
    @classmethod
    def show(self):
        print(f"The class value of a is {self.a}")

e = Employee()
e.a = 45
e.show()