# 4. Write a program to sum a list with 4 numbers.
# Create an empty list
numbers = []

# Take 4 numbers from the user
for i in range(4):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate the sum
total = sum(numbers)

# Display the result
print("\nNumbers entered:", numbers)
print("Sum of numbers:", total)
