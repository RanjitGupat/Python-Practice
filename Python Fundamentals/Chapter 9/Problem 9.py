# 9. Write a program to find out whether a file is identical & matches the content of
# another file.


with open("file.txt") as f:
    content = f.read()

with open("log_copy.txt") as f:
    content1 = f.read()

if(content == content1):
    print("Yes these file are identical")
else:
    print("No these file are not identical.")
