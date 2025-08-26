class Employee:
    language = "Python"   # This is a class attribute
    salary = 12000
    
    # self refers to the instance of the class. It is automatically passed with a function call
    # from an object.
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet():  #self use kar ke argument get kar skate hai
        print("Good morning")

ranjit = Employee()
ranjit.language = "js"    # this is a instance attribute
ranjit.getInfo()
#Employee.getInfo(ranjit)

ranjit.greet()
#Employee.getInfo(ranjit) argument pass kar diya 