# PROJECT 2 – THE PERFECT GUESS
# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.
# Hint: Use the random module.


import random   # Importing the random module to generate random numbers

# Generate a random number between 1 and 100 (both inclusive)
n = random.randint(1, 100)

a = -1          # Initialize user's guess with -1 (so it never equals n initially)
guesses = 1     # Counter to keep track of number of guesses (start from 1)

# Loop until the user guesses the correct number
while(a != n):
    
    a = int(input("Guess the number: "))   # Take user input and convert it to integer
    
    if(a > n):                            # If guess is greater than the secret number
        print("Lower number please")      # Hint: guess a smaller number
        guesses += 1                      # Increase guess count
    
    elif(a < n):                          # If guess is smaller than the secret number
        print("Higher number please")     # Hint: guess a larger number
        guesses += 1                      # Increase guess count

# When the loop ends, it means user guessed correctly
print(f"You have guessed the number {n} correctly in {guesses} attempts")
