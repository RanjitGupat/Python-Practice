# 1. Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Programer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
          

p = Programer("Ranjit", 1200000, 212402)
print(p.name, p.salary, p.pin, p.company)

p = Programer("Shobhit", 3500000, 212404)
print(p.name, p.salary, p.pin, p.company)