# Creating a tuple
my_tuple = (10, 20, 30, 20, 40, 20)

# 1. count(x) → Returns the number of times x appears in the tuple
count_20 = my_tuple.count(20)
print("count of 20:", count_20)
# Output: 3
# Explanation: '20' appears 3 times in the tuple.

# 2. index(x, [start], [end]) → Returns the first index of x
pos_30 = my_tuple.index(30)
print("index of 30:", pos_30)
# Output: 2
# Explanation: '30' is at index position 2.

# With optional start & end parameters
pos_20_after_index2 = my_tuple.index(20, 3)  # start searching from index 3
print("index of 20 after index 3:", pos_20_after_index2)
# Output: 3


print(len(my_tuple))