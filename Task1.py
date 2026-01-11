import random

# Step 1: Predefined list of words
words = ["python", "hangman", "programming", "code", "developer"]

# Step 2: Randomly select a word
secret_word = random.choice(words)

# Step 3: Game variables
guessed_letters = set()
attempts = 6

print(" Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

# Step 4: Game loop
while attempts > 0:
    display_word = ""

    # Show guessed letters or underscores
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Attempts left:", attempts)

    # Check if user has guessed the whole word
    if "_" not in display_word:
        print(" Congratulations! You guessed the word correctly.")
        break

    # Step 5: Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    # Step 6: Check guess
    if guess not in secret_word:
        attempts -= 1
        print(" Wrong guess!")

# Step 7: Game over
if attempts == 0:
    print("\n Game Over! The word was:", secret_word)
