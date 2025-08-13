# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# Taking marks as input
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

# Assuming each subject is out of 100 marks
total_marks = sub1 + sub2 + sub3
percentage = (total_marks / 300) * 100  # 3 subjects × 100 marks each

# Checking conditions
if sub1 < 33 or sub2 < 33 or sub3 < 33:
    print("Fail: You scored less than 33% in one or more subjects.")
elif percentage < 40:
    print("Fail: Your total percentage is less than 40%.")
else:
    print("Pass! Congratulations ")
