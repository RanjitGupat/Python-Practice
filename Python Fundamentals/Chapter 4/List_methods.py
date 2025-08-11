# 1. append(x) → Add a single element at the end
fruits = ["apple", "banana"]
fruits.append("cherry")
print("append:", fruits)  
# ['apple', 'banana', 'cherry']

# 2. extend(iterable) → Add multiple elements from another iterable
fruits.extend(["mango", "orange"])
print("extend:", fruits)  
# ['apple', 'banana', 'cherry', 'mango', 'orange']

# 3. insert(index, x) → Insert element at a specific position
fruits.insert(1, "grapes")
print("insert:", fruits)  
# ['apple', 'grapes', 'banana', 'cherry', 'mango', 'orange']

# 4. remove(x) → Remove first occurrence of value x
fruits.remove("banana")
print("remove:", fruits)  
# ['apple', 'grapes', 'cherry', 'mango', 'orange']

# 5. pop([index]) → Remove and return element at index (last if not given)
last_item = fruits.pop()
print("pop (last item):", last_item)
print("after pop:", fruits)  
# 'orange'
# ['apple', 'grapes', 'cherry', 'mango']

# 6. clear() → Remove all elements
temp = fruits.copy()
temp.clear()
print("clear:", temp)  
# []

# 7. index(x, [start], [end]) → Find index of first occurrence
numbers = [10, 20, 30, 20, 40]
pos = numbers.index(20)  
print("index of 20:", pos)  
# 1

# 8. count(x) → Count occurrences of a value
count_20 = numbers.count(20)
print("count of 20:", count_20)  
# 2

# 9. sort(key=None, reverse=False) → Sort in ascending order by default
numbers.sort()
print("sorted:", numbers)  
# [10, 20, 20, 30, 40]

# Sort in reverse
numbers.sort(reverse=True)
print("sorted reverse:", numbers)  
# [40, 30, 20, 20, 10]

# 10. reverse() → Reverse the list order
letters = ['a', 'b', 'c']
letters.reverse()
print("reverse:", letters)  
# ['c', 'b', 'a']

# 11. copy() → Make a shallow copy
original = [1, 2, 3]
copied = original.copy()
print("copy:", copied)  
# [1, 2, 3]
