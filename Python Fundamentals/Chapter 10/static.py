class Employee:
    language = "Python"   # This is a class attribute
    salary = 12000
    
    # Sometimes we need a function that does not use the self-parameter. We can define a
    # static method like this:

    @staticmethod
    def greet():  
        print("Good morning")


ranjit = Employee()
ranjit.greet()   # We can call this without argument using staticmethod.