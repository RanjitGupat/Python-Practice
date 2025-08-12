# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

d = {}

for i in range(4):
    name = input(f"Enter friends name {i+1} : ")
    lang = input(f"Enter Language name {i +1} : ")
    d.update({name:lang})

print(d)