import random

def jumble_word(word):
    word = list(word)  # Convert the word to a list of characters
    random.shuffle(word)  # Shuffle the list of characters
    return ''.join(word)  # Convert the list of characters back to a string

# List of words for the game
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Randomly select a word from the list
selected_word = random.choice(words)

# Jumble the selected word
jumbled_word = jumble_word(selected_word)

# Display the jumbled word to the player and ask for their guess
print(f"Guess the word: {jumbled_word}")
guess = input("Your guess: ")

# Check the player's guess
if guess == selected_word:
    print("Congratulations! That's correct.")
else:
    print(f"Sorry, that's incorrect. The word was: {selected_word}")

