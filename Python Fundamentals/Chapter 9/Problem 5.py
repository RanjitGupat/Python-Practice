# 5. Repeat program 4 for a list of such words to be censored.

words = ["Donkey", "ganda", "bad"]

with open("file1.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"*len(word))

with open("file1.txt", "w") as f:
    f.write(content)