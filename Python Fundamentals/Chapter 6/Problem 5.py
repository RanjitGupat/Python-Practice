# 5. Write a program which finds out whether a given name is present in a list or not

# Predefined list of names
names = ["Ravi", "Ranjit", "Anita", "Suman", "Priya"]

# Taking name as input
name_to_check = input("Enter the name to search: ")

# Check if the name is in the list
if name_to_check in names:
    print(f"{name_to_check} is present in the list.")
else:
    print(f"{name_to_check} is NOT present in the list.")
