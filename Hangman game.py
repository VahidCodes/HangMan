import random

# List of words for the game
words = ['python', 'java', 'swift', 'javascript', 'hangman']

def get_random_word(word_list):
    """Selects a random word from the list of words."""
    return random.choice(word_list)

def display_board(word, guessed_letters):
    """Displays the current state of the game board."""
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print('Current word: ', display_word)
    print('Guessed letters: ', ' '.join(guessed_letters))

def get_guess():
    """Prompts the user for a guess and returns it."""
    guess = input('Enter a letter: ').lower()
    while len(guess) != 1 or not guess.isalpha():
        guess = input('Invalid input. Please enter a single letter: ').lower()
    return guess

def play_hangman():
    word = get_random_word(words)
    guessed_letters = set()
    attempts = 6

    print('Welcome to Hangman!')
    print('You have 6 attempts to guess the word.')

    while attempts > 0:
        display_board(word, guessed_letters)
        guess = get_guess()

        if guess in guessed_letters:
            print('You already guessed that letter.')
        elif guess in word:
            print('Good guess!')
            guessed_letters.add(guess)
        else:
            print('Incorrect guess.')
            guessed_letters.add(guess)
            attempts -= 1
            print(f'You have {attempts} attempts left.')

        if all(letter in guessed_letters for letter in word):
            print('Congratulations! You guessed the word:', word)
            break
    else:
        print('Sorry, you ran out of attempts. The word was:', word)

play_hangman()
