# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

# Template
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

# Taking inputs from user
name = input("Enter your name: ")
date = input("Enter the date: ")

# Replacing placeholders with actual values
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)

# Displaying final letter
print(letter)
