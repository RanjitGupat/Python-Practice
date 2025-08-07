# 4. Write a python program to print the contents of a directory using 
# the os module. 
# Search online for the function which does that. 

# Import the os module which provides functions for interacting with the operating system
import os

# Set the directory path ('.' means current directory)
path = '/'

# Get the list of all files and directories in the given path using os.listdir()
contents = os.listdir(path)

# Print a message before listing contents
print("Contents of the directory:")

# Loop through the list and print each item
for item in contents:
    print(item)
