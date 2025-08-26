class Employee:
    language = "Python"   # This is a class attribute
    salary = 12000

ranjit = Employee()
ranjit.name = "Ranjit"    # This is a instance(object) attribute
print(ranjit.name, ranjit.language, ranjit.salary)

shobhit = Employee()
shobhit.name = "Shobhit"
print(shobhit.name, shobhit.language, shobhit.salary)

# Here name is instance(object) attribute and salary and 
# language are class attribute and as 
# they directly belong to the class.
