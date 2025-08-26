# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a = 4

o = Demo()
print(o.a) # Prints the class attribute becasue instance attribute in not present.

o.a = 0   # Instance attribute is set
print(o.a) # Prints the instance attribute becasue instance attribute in  present.

print(Demo.a)  #Prints the class attribute