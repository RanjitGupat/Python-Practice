# Strings in Python are IMMUTABLE — meaning they cannot be changed after creation.

name = "Ranjit"

# ❌ Trying to change a single character will cause an error
# name[0] = "S"  # Uncommenting this will give: TypeError: 'str' object does not support item assignment

# ✅ Instead, any "modification" creates a NEW string object
new_name = name.replace("R", "S")  # This returns a new string, original remains same

print("Original string:", name)      # Output: Ranjit
print("New string:", new_name)       # Output: Sanjit

# Let's check memory addresses using id()
print("Memory address of 'name':", id(name))
print("Memory address of 'new_name':", id(new_name))
# Notice: They have different memory addresses → proves a new string was created
