a = int(input("Enter your age: "))
if(a >= 18):
    print("You are above the age of consent")
    print("Good for you")
elif(a < 0):      # this ladder will stop once a condition in an if or 

    print("you are entering an invalid age.")
elif(a == 0):
    print("Your are entering 0 which is not a valid age.")
else:
    print("You are below the age consent")

print("end of program")