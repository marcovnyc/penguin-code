import random

def get_shuffled_choices(favorite, all_fruits):
    """Returns a shuffled list containing the favorite fruit and some other random fruits."""
    choices = [favorite]
    while len(choices) < 4:  # Assuming we want 4 choices
        fruit = random.choice(all_fruits)
        if fruit not in choices:
            choices.append(fruit)
    random.shuffle(choices)
    return choices

# Dictionary of animals and their favorite fruits
favorite_fruits = {
    "monkey": "banana",
    "elephant": "apple",
    "parrot": "cherry",
    "koala": "eucalyptus"  # Technically not a fruit, but for fun!
}

# List of all fruits (including some extras to offer as wrong choices)
all_fruits = ["banana", "apple", "cherry", "grape", "orange", "pear", "eucalyptus"]

# Randomly select an animal
animal = random.choice(list(favorite_fruits.keys()))

# Get shuffled fruit choices for the player
choices = get_shuffled_choices(favorite_fruits[animal], all_fruits)

# Present the choices to the player
print(f"What is the favorite fruit of a {animal}?")
for i, choice in enumerate(choices, 1):
    print(f"{i}. {choice}")

# Get the player's guess
guess = int(input("Enter the number of your choice: "))

# Check the answer
if choices[guess-1] == favorite_fruits[animal]:
    print("Correct! Well done!")
else:
    print(f"Oops! A {animal} actually loves {favorite_fruits[animal]}.")

