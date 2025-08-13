# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams


# Taking comment as input
comment = input("Enter your comment: ").lower()  # convert to lowercase for easy matching

# Spam keywords
spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

# Check if comment contains any spam keyword
is_spam = False
for keyword in spam_keywords:
    if keyword in comment:
        is_spam = True
        break  # no need to check further

# Output result
if is_spam:
    print("This comment is spam!")
else:
    print("This comment is not spam.")
