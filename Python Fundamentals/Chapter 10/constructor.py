# __init__() is a special method which is first run as soon as the object is created.
# __init__() method is also known as constructor.

class Employee:
    language = "Python"   # This is a class attribute
    salary = 12000

    def __init__(self, name, salary, language):   # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object.")

ranjit = Employee("Ranjit", 130000, "Python")
#ranjit.name = "Ranjit"    # This is a instance(object) attribute
print(ranjit.name, ranjit.language, ranjit.salary)
