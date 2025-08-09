# 3. Write a program to detect double space in a string.

# Taking input from user
text = input("Enter a string: ")

# Using find() to locate double space
position = text.find("  ")  # Returns -1 if not found

if position != -1:
    print(f"Double space found at index {position}")
else:
    print("No double space found.")
