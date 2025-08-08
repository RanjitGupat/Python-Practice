# type() function is used to find the data type of a given variable in python.
a = 31
t = type(a) # class <int>
print(t)
b = "31"
x = type (b) # class <str>
print(x)
c = 3.4
y = type (c) # class float>
print(y)

d = True
w = type (d) # class float>
print(w)

# A number can be converted into a string and vice versa (if possible)
# There are many functions to convert one data type into another.
a = 31
t = str(a)    # integer to string conversion "31"
print(type(t),"=",t)

b = "32"
r = int(b)    # string to integer conversion 32
print(type(r),"=",r)

c = 45
y = float(c)  # integer to float conversion 45.0
print(type(y),"=",y)
# … and so, on
# Here "31" is a string literal and 31 a numeric literal.