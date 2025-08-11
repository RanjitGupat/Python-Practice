# 2. Write a program to accept marks of 6 students and display them in a sorted
# manner.

# Loop to take 7 fruit names from user
marks = []
for i in range(6):
    mark = int(input(f"Enter marks students  {i+1}: "))
    marks.append(mark)

marks.sort()

# Display the list of fruits
print("\nList of fruits entered:", marks)

# How it works
# fruits = [] → Creates an empty list.

# for i in range(7): → Loops exactly 7 times.

# input() → Takes fruit name from user.

# append() → Adds each fruit to the list.

# Print → Shows the final list.