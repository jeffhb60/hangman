import random

def hangman():
    word_list = ['python', 'hangman', 'code', 'developer', 'programming', 'computer']
    word = random.choice(word_list)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")
    print(" ".join(guessed_word))

    while attempts > 0 and '_' in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        print(" ".join(guessed_word))

    if '_' not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)

# Run the game
hangman()
