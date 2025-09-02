# Variable with type hint
n : int = 5        # n is expected to be an integer, here assigned value 5

# Another variable with type hint
name : str = "Ranjit"   # name is expected to be a string, here assigned "Ranjit"

# Function with type hints
def sum(a : int, b : int) -> int:   # a and b should be integers, function returns an integer
    return a + b                    # returns the sum of a and b

# Example usage
print(sum(3, 4))   # Correct: both are integers, output = 7
# print(sum("3", "4"))  # Wrong: type checker will complain (expected int, got str)


