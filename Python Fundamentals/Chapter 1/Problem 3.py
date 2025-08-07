# 3. Install an external module and use it to perform an operation of your interest.  
# pip install pyttsx3

import pyttsx3

engine = pyttsx3.init()
text = input("Enter :")
engine.say(text)
engine.runAndWait()