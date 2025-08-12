# What is a Set in Python?
# A set is a built-in Python data type used to store multiple unique values.

# Unordered → Elements don’t have a fixed position.

# Unindexed → No element can be accessed by index like lists or tuples.

# Mutable → You can add or remove items.

# No duplicates allowed → If you try to add a duplicate, it’s ignored.


e = set()    # Don't use s={} as it will create an empty dictionary
s = {1, 3, 4, 4, 45, 45, 57}
print(s)
# output : {1, 3, 4, 57, 45}



# PROPERTIES OF SETS
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.