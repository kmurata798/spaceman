import random

secret_word = list()
underscored_word = list()
letters_guessed = list()

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
#Loop through secret_word list and compare with letters_guessed list to see whether they are the same
    for letter in secret_word:
        if input_word[letter] == given_word[letter]:
            return True
        else:
            retletters_guessed
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
#loop through secret_word list and compare with letters_guessed list to see whether they are the same.
#If so, change the index in the underscored_word the same value as the 
    for letter in secret_word:
        if input_word[letter] == given_word[letter]:
            underscored_word[letter] = given_word[letter]
            return str(underscored_word)
        else:
            return str(underscored_word)

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''

#loop through secret_word list and compare whether the input letter matches any of the letters in the secret_word list
    for letter in secret_word:
        if guess == secret_word[letter]:
            return True
        else:
            return False

    #TODO: check if the letter guess is in the secret word

    de f play_again():
        ans = input("Would you like to play again?: (Y for yes / N for no)")
        if ans == 'Y' or ans == 'y':
            return True
        if ans == 'N' or ans == 'n':
            return False


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''

    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =\nSpaceman is a guessing game. There is a mystery word which the user tries to guess one letter at a time.\nA placeholder is initially shown, with the number of blanks corresponding to the number of letters in the word. \nIf the letter is in the mystery word, the position(s) of the letter(s) are revealed in the placeholders.\nGuess the word before you run out of guesses! \n \nUsers win if they can guess the mystery word before the spaceman is drawn. \nThe spaceman is made up of seven parts, and each part is drawn for each incorrect guess. \nIf all seven parts get drawn before the user guesses the word, then they lose.")
    #TODO: show the player information about the game according to the project spec
    
    print("^-------------------------------------------------------------------------------------------------------------^\n\nPlease enter the letter you want to guess: ")

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost

    running = True
    while running:
        spaceman(load_word())
        running = play_again() 





#These function calls that will start the game
#secret_word = load_word()
#spaceman(load_word())

print(load_word())