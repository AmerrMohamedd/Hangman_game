# The Hangman program randomly selects a secret word from a list of secret words.
# The Game: Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.
# When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way,all letters of the word are to be guessed before all the chances are over.
# For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five letters word.

import random

words = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
word_list = words.split()


def choose_random_word():
    return random.choice(word_list)


def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display


def hangman():
    secret_word = choose_random_word().lower()
    guessed_letters = []
    max_attempts = len(secret_word) + 2
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(secret_word, guessed_letters))

    while '_' in display_word(secret_word, guessed_letters):
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!")
        else:
            print("Incorrect guess.")
            attempts += 1

        print(display_word(secret_word, guessed_letters))

        if attempts >= max_attempts:
            print("Sorry, you've run out of attempts!")
            print("The word was:", secret_word)
            break

    if '_' not in display_word(secret_word, guessed_letters):
        print("Congratulations! You guessed the word:", secret_word)


if __name__ == '__main__':
    hangman()
