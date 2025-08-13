# Quick Quiz: Write a program to print yes when the age entered by the user is greater
# than or equal to 18.

a = int(input("Enter your age: "))
if(a >= 18):
    print("Yes")
    
elif(a < 0):      # this ladder will stop once a condition in an if or 

    print("you are entering an invalid age.")
elif(a == 0):
    print("Your are entering 0 which is not a valid age.")
else:
    print("no")

print("end of program")