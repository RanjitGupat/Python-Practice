# 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).

s = set()

#  Take 8 numbers from the user
for i in range(8):
    num = int(input(f"Enter number {i+1}: "))
    s.add(num)  # Set will automatically remove duplicates

# Display unique numbers
print("Unique numbers are:", s)

