import random
#Secret Word list
secret_word = list()

#generate a random word
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
        if letter not in letters_guessed:
            return False
    return True
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    letters_guess_so_far = []
    for letter in secret_word:
        if letter in letters_guessed:
            letters_guess_so_far.append(letter)
        else:
            letters_guess_so_far.append("_")
    return letters_guess_so_far

#loop through secret_word list and compare with letters_guessed list to see whether they are the same.
#If so, change the index in secret_word to the same value as the 

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

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
        if letter == guess:
            return True
    return False

    #TODO: check if the letter guess is in the secret word

def play_again():
    while True: 
        ans = input("Would you like to play again?: ( Y = yes )( N = no ): ")
        if ans == 'Y' or ans == 'y':
            print("\n\nAgain!? OoooOKAY!\n\n")
            return True
        elif ans == 'N' or ans == 'n':
            print("Hope you had FUN! Bye!")
            return False
        else:
            print("Please enter either: ( Y or N )")

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =\nWelcome to Spaceman!\nYou have 7 incorrect guesses, please enter one letter per round!")
    #TODO: show the player information about the game according to the project spec
    
    attempts = 6
    retry = True
    letters_guessed = [] # letters correct
    word_bank = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] #letters not guessed yet
    while retry:
            
        guess = input("-----------------\nEnter your guess: ") 
        #User's input

        if len(guess) != 1:
            print("\nPlease type ONE letter!")
        #TODO: Ask the player to guess one letter per round and check that it is only one letter

        if guess not in word_bank:
            print("\nYou have already used this letter")
            print(''.join(get_guessed_word(secret_word, letters_guessed)))
            continue
        #check if user's input is a duplicate

        if guess in word_bank:
            word_bank.remove(guess)
        #whenever the user guesses a letter, take the letter off the wordbank

        if is_guess_in_word(guess, secret_word) == True:
            letters_guessed.append(guess)
            print("\nYour guess appears in the word!\nGuessed word so far: ")
            print(''.join(get_guessed_word(secret_word, letters_guessed)))
                #TODO: Check if the guessed letter is in the secret or not and give the player feedback
                #TODO: show the guessed word so far
            if is_word_guessed(secret_word, letters_guessed):
                print(f"\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nThe word was {secret_word}!\nYOU WIN!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
                break
            #Determine if game is won

            print("These letters haven't been guessed yet: " + ''.join(str(w) for w in word_bank))

        else:
            if attempts == 0:
                print("\n\n^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^\n\nOH NO! You ran out of attempts!\n\n ___[-GAME OVER-]___\n\nhe word was: [ " + secret_word + " ]\n\n^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^\n")
                retry = False
                #check if user has lost the game
            else:
                attempts = attempts - 1
                print (f"\nSorry your guess was not in the word, try again.\nYou have {attempts + 1} incorrect guesses left!\nGuessed word so far: ")
                print(''.join(get_guessed_word(secret_word, letters_guessed)))
                print("These letters haven't been guessed yet: " + ''.join(str(e) for e in word_bank) + "\n")
                #If the user inputs a wrong guess
    
            #TODO: check if the game has been won or lost


running = True
while running:
    spaceman(load_word())
    running = play_again() 

#loop the game until play again == False





#These function calls that will start the game
#secret_word = load_word()
#spaceman(load_word())

#print(load_word())