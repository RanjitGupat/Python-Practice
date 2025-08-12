# 8. If languages of two friends are same; what will happen to the program in problem
# 6?

fav_lang = {}

fav_lang["Ravi"] = "Python"
fav_lang["Amit"] = "Java"
fav_lang["Sumit"] = "Python"  # Same language as Ravi
fav_lang["Neha"] = "Java"     # Same language as Amit

print(fav_lang)


# "Ravi" and "Sumit" are different keys (names), but they both have "Python" as the value. ✅ Allowed.

# "Amit" and "Neha" also share "Java". ✅ Allowed.

# Dictionaries only enforce uniqueness on keys, not on values.