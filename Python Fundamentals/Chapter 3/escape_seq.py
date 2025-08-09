# 1. \n – New line (moves to next line)
print("Hello\nWorld")
# Output:
# Hello
# World

# 2. \t – Horizontal tab (adds space like a tab key)
print("Hello\tWorld")
# Output: Hello   World

# 3. \\ – Backslash (prints a single backslash)
print("This is a backslash: \\")
# Output: This is a backslash: \

# 4. \' – Single quote
print('It\'s a good day')
# Output: It's a good day

# 5. \" – Double quote
print("He said, \"Python is awesome!\"")
# Output: He said, "Python is awesome!"

# 6. \r – Carriage return (moves cursor to the start of the line, overwrites text)
print("Hello\rWorld")
# Output: World   (overwrites Hello with World)

# 7. \b – Backspace (deletes one character before cursor)
print("Hello\bWorld")
# Output: HellWorld

# 8. \f – Form feed (moves to next "page" in some printers / not common in consoles)
print("Hello\fWorld")
# Output may appear as: HelloWorld (depends on environment)

# 9. \v – Vertical tab (moves text down without starting new paragraph)
print("Hello\vWorld")
# Output may appear as:
# Hello
#       World

# 10. \ooo – Character with octal value
print("\101")   # A in ASCII
# Output: A

# 11. \xhh – Character with hexadecimal value
print("\x41")   # A in ASCII
# Output: A
