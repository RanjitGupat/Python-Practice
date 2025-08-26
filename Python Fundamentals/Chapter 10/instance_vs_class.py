class Employee:
    language = "Python"   # This is a class attribute
    salary = 12000

ranjit = Employee()
ranjit.language = "js"    # this is a instance attribute
print(ranjit.language, ranjit.salary)