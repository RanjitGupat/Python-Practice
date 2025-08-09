name = "  Ranjit Kumar  "

# 1. strip(), lstrip(), rstrip() – remove spaces (or specified characters)
print(name.strip())    # Removes spaces from both sides → 'Ranjit Kumar'
print(name.lstrip())   # Removes spaces from the left side only
print(name.rstrip())   # Removes spaces from the right side only

# 2. lower() – convert all characters to lowercase
print(name.lower())    # → '  ranjit kumar  '

# 3. upper() – convert all characters to uppercase
print(name.upper())    # → '  RANJIT KUMAR  '

# 4. title() – capitalize the first letter of each word
print(name.title())    # → '  Ranjit Kumar  '

# 5. swapcase() – swap uppercase to lowercase and vice versa
print(name.swapcase()) # → '  rANJIT kUMAR  '

# 6. isalpha() – check if all characters are alphabets (no spaces, digits, or symbols)
print("Ranjit".isalpha())    # True  (all alphabets)
print("Ranjit123".isalpha()) # False (contains numbers)

# 7. isdigit() – check if all characters are digits
print("12345".isdigit())     # True
print("12a45".isdigit())     # False (contains a letter)

# 8. isnumeric() – check if string is numeric (digits + numeric symbols like ½, ²)
print("¾".isnumeric())       # True

# 9. isalnum() – check if all characters are alphabets or digits (no spaces/symbols)
print("Ranjit123".isalnum()) # True
print("Ranjit 123".isalnum())# False (contains a space)

# 10. split() – split string into list using spaces (or custom separator)
print(name.split())          # ['Ranjit', 'Kumar']

# 11. join() – join list elements into string using a separator
words = ["Hello", "World"]
print(" ".join(words))       # 'Hello World'

# 12. zfill(width) – add leading zeros to make total length = width
print("42".zfill(5))         # '00042'

# 13. center(width, char) – center text and fill sides with given char
print("Hi".center(10, "-"))  # '----Hi----'

# 14. startswith() – check if string starts with given text (can use position)
print(name.strip().startswith("Ranj")) # True

# 15. endswith() – check if string ends with given text (can use position range)
print(name.strip().endswith("jit"))    # True

# 16. replace(old, new) – replace all occurrences of old with new
print(name.replace("Ranjit", "Sanjay")) # '  Sanjay Kumar  '

# 17. find(sub) – return index of first occurrence, or -1 if not found
print(name.find("Kumar"))              # 9

# 18. rfind(sub) – return index of last occurrence
print("banana".rfind("a"))             # 5

# 19. count(sub) – count how many times a substring occurs
print("banana".count("a"))             # 3

# 20. partition(sep) – split into tuple: (before, sep, after)
print("apple-orange".partition("-"))   # ('apple', '-', 'orange')

# 21. rpartition(sep) – split at last occurrence of separator
print("apple-orange-mango".rpartition("-")) # ('apple-orange', '-', 'mango')

# 22. expandtabs(tabsize) – replace \t with spaces (default 8 spaces)
print("Hello\tWorld".expandtabs(4))    # 'Hello   World'

# 23. encode() – encode string into bytes
print("Ranjit".encode())               # b'Ranjit'

# 24. format() – insert values into placeholders
print("My name is {}".format("Ranjit"))   # 'My name is Ranjit'

# 25. maketrans() + translate() – replace multiple characters at once
trans = str.maketrans("aeiou", "12345")   # mapping vowels to numbers
print("apple".translate(trans))           # '1ppl2'
