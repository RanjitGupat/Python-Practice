s = {1, 3, 4, 4, 45, 45, 57, "Ranjit"}
print(s,type(s))

s.add(566)
print(s,type(s))


# all methods

A = {1, 2, 3}
B = {3, 4, 5}

# Adding elements
A.add(6)                      # {1, 2, 3, 6}
A.update([7, 8])               # {1, 2, 3, 6, 7, 8}

# Copy
C = A.copy()

# Difference
print(A.difference(B))         # {1, 2, 6, 7, 8}
A.difference_update(B)         # removes 3

# Discard & Remove
A.discard(100)                 # no error
# A.remove(100)                # KeyError if uncommented

# Intersection
print(C.intersection(B))       # {3}
C.intersection_update(B)       # keeps only common elements

# Relations
print(A.isdisjoint({9, 10}))   # True
print({1, 2}.issubset(A))      # True or False depending on A
print(A.issuperset({1}))       # True

# Pop
value = A.pop()

# Symmetric Difference
print({1, 2}.symmetric_difference({2, 3})) # {1, 3}

# Union
print({1, 2}.union({2, 3}))    # {1, 2, 3}

# Clear
A.clear()
