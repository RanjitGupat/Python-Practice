# String is a data type in python.
# String is a sequence of characters enclosed in quotes.
# We can primarily write a string in these three ways.



name = "Ranjit"   # Single quoted string
a = 'Shobhit'     # Double quoted string
n = '''ranjit'''  # Triple quoted string

nameshort = name[0:3] # start from index 0 all the way till 3 (exclyding)
print(nameshort)
c = len(name)
print(c)

print(name[-6:-1])
print(name[0:6])
print(name[-6:])
print(name[:6])



# SLICING WITH SKIP VALUE
# We can provide a skip value as a part of our slice like this:
word = "amazing"
word[1: 6: 2] # "mzn"
# Other advanced slicing techniques:
Word = "amazing"
print(Word[:7]) # word [0:7] – 'amazing'
print(Word[0:])# word [0:7] – 'amazing'