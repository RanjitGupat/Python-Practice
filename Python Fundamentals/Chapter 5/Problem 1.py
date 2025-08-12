# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up! 

# Hindi to English dictionary
hindi_dict = {
    "pustak": "book",
    "kutta": "dog",
    "billi": "cat",
    "ghar": "house",
    "paani": "water",
    "roti": "bread"
}

# word = input("Enter the word you want meaning of : ")
# print(hindi_dict[word])


#seconds methods

# Display the words available
print("Available Hindi words:", list(hindi_dict.keys()))

# Take input from user
word = input("Enter a Hindi word to find its English meaning: ").strip().lower()

# Lookup the word
meaning = hindi_dict.get(word)

# Show result
if meaning:
    print(f"The English meaning of '{word}' is '{meaning}'.")
else:
    print(f"Sorry! '{word}' is not in the dictionary.")