# De originele versie van hangman. PAS DIT BESTAND NIET AAN.
#
# De knop compare draait dit programma en jouw hangman.py met dezelfde
# antwoorden, en vergelijkt wat ze printen. Verander je dit bestand, dan
# valt er niets meer te vergelijken.

import random


def hangman_game() -> None:
    print("WELCOME TO HANGMAN ツ")

    # Prompt and re-prompt for word length
    word_length = int(input("What length of word would you like to play with?\n"))
    while word_length > 44 or word_length <= 0:
        word_length = int(input("Invalid word length! Please enter a length between 1 and 44.\n"))

    # Load words
    words: set[str] = set()
    with open('dictionary.txt', "r") as file:
        for line in file:
            word = line.rstrip()
            if len(word) == word_length:
                words.add(word)

    # Prompt and re-prompt for number of guesses
    number_guesses = int(input("How many guesses are allowed?\n"))
    while number_guesses <= 0:
        number_guesses = int(input("Negative or zero guesses make no sense.\n"))

    # Run an infinite number of games
    while True:
        # Game set-up
        print(f"I have a word in my mind of {word_length} letters.")
        word = random.choice(list(words))
        guesses: set[str] = set()
        correct_guesses: set[str] = set()
        current_guesses = number_guesses

        # Allow guessing and provide guesses to the game
        while current_guesses > 0:
            guessed_all = True
            for letter in word:
                if letter not in correct_guesses:
                    guessed_all = False
                    break
            if guessed_all:
                break

            # Prompt and re-prompt for single letter
            letter = input(f"Guess a letter ({current_guesses} left): ")
            if len(letter) != 1 or not letter.isalpha() or letter in guesses:
                continue

            guesses.add(letter)
            if letter in word:
                correct_guesses.add(letter)
                print("It's in the word! :)")
            else:
                current_guesses -= 1
                print("That's not in the word :(")

            current_pattern = ''
            for letter in word:
                if letter in correct_guesses:
                    current_pattern += letter
                else:
                    current_pattern += '_'
            print(current_pattern)

        # After game ends, present the conclusion
        guessed_all = True
        for letter in word:
            if letter not in correct_guesses:
                guessed_all = False
                break

        if guessed_all:
            print("Whoa, you won!!!")
            break
        else:
            print(f"Sad, you lost ¯\\_(ツ)_/¯. This was your word: {word}")
            break


if __name__ == '__main__':
    hangman_game()
