try:
    # Example 1: Division by zero error
    num = int(input("Enter a number: "))
    result = 10 / num   # If num = 0 → ZeroDivisionError

    # Example 2: File handling error
    with open("data.txt") as f:   # If file not found → FileNotFoundError
        content = f.read()

    # Example 3: Type error
    print("Result: " + result)  # Cannot add string + int/float → TypeError

# Handle specific exceptions one by one
except ZeroDivisionError:
    print("Error: You tried dividing by zero!")

except FileNotFoundError:
    print("Error: The file 'data.txt' was not found!")

except TypeError:
    print("Error: Invalid operation between different data types!")

# Catch any other unexpected exception
except Exception as e:
    print("Unexpected error:", e)

# Finally block (optional) → always runs
finally:
    print("Program finished (with or without error).")
