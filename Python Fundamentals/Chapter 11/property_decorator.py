



class Employee:
    a = 1
    @classmethod
    def show(self):
        print(f"The class value of a is {self.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname} "
    
    @name.setter
    def name (self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Ranjit Gupta"
print(e.fname, e.lname)

e.show()