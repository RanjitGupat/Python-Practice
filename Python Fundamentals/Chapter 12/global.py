a = 100 # global variable

def fun():
    # global a
    a = 3  # local variable
    print(a)

print(a)
fun()


# ‘global’ keyword is used to modify the variable outside of the current scope.