marks = {
    "Ranjit":83,
    "Shobhit":70,
    "Shivam":98,
    "Himanshu":95,
    "list":[1,2,3,4]
}

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Shivam":96})

print(marks.get("Himanshu"))

#if 
print(marks.get("Himanshu1"))   #print none
print(marks["Himanshu1"])       #retrun error  

print(marks)



# Dictionary Methods in Python, Example with All Methods

# Example dictionary
d = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 1. clear()
d_copy = d.copy()
d_copy.clear()
print("clear():", d_copy)  # {}

# 2. copy()
d2 = d.copy()
print("copy():", d2)

# 3. fromkeys()
print("fromkeys():", dict.fromkeys(['a', 'b', 'c'], 0))

# 4. get()
print("get():", d.get('age', 'Not Found'))  # 25
print("get() missing:", d.get('salary', 'Not Found'))  # Not Found

# 5. items()
print("items():", list(d.items()))

# 6. keys()
print("keys():", list(d.keys()))

# 7. pop()
print("pop():", d.pop('city', 'No Key'))  # New York
print("After pop:", d)

# 8. popitem()
print("popitem():", d.popitem())  # ('age', 25)

# 9. setdefault()
print("setdefault():", d.setdefault('country', 'USA'))
print("After setdefault:", d)

# 10. update()
d.update({'name': 'Bob', 'salary': 50000})
print("update():", d)

# 11. values()
print("values():", list(d.values()))

