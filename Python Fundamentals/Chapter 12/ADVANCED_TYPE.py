from typing import List, Tuple, Dict, Union   # Import type hint classes from typing module

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]  
# Here numbers is a list where each element must be an integer

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)  
# person is a tuple with exactly two values:
# - First value must be a string ("Alice")
# - Second value must be an integer (30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}  
# scores is a dictionary where:
# - Keys must be strings ("Alice", "Bob")
# - Values must be integers (90, 85)

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"  
# identifier can either be an integer OR a string
# Here it holds a string value ("ID123")

identifier = 12345  
# This is also valid because identifier can be an int as well
