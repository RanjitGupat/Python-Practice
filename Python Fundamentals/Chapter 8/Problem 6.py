# 6. Write a python function which converts inches to cms.
# 1 inch = 2.54 cm

def inches_to_cm(inches):
    return inches * 2.54

# Example usage
inch_value = int(input("Enter length in inches : "))
print(inch_value, "inches =", inches_to_cm(inch_value), "cm")
