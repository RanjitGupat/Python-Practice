# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1,2]}
s[4][0] =9 #type error

# will give an error before you even get the chance to change anything.

# Why?
# Sets in Python can only contain hashable (immutable) objects.

# A list ([1, 2]) is mutable → you can change it, so it is unhashable.

# Because of that, you cannot store a list inside a set at all.

