# 7. Write a program to find out whether a given post is talking about “Ranjit” or not.

# Taking post content as input
post = input("Enter your post: ").lower()  # convert to lowercase for case-insensitive search

# Check if "ranjit" is mentioned
if "ranjit" in post:
    print("This post is talking about Ranjit.")
else:
    print("This post is not talking about Ranjit.")
