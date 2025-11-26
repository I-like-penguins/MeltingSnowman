import ascii_art
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(ascii_art.STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    right_letters = []
    mistakes = 0
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line
    while mistakes < 3 or "_" in secret_word:
        display_game_state(mistakes, secret_word, guessed_letters)

        # For now, simply prompt the user once:
        guess = input("Guess a letter: ").lower()
        if guess[0].isalpha() == False:
            print("Please enter a single letter.")
            continue
        guessed_letters.append(guess[0])
        print("You guessed:", guess)
        if guess not in secret_word:
            mistakes += 1
        else:
            for i in range(secret_word.count(guess)): # multiple occurrences of the same letter
                right_letters.append(guess)
            if len(right_letters) == len(secret_word):
                display_game_state(mistakes, secret_word, guessed_letters)
                print("You won!")
                return

    display_game_state(mistakes, secret_word, guessed_letters)
    print("You lost!")