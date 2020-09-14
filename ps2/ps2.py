# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

letters_guessed=[]
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    n=0
    for char1 in secret_word:
        for char2 in letters_guessed:
            if char1 == char2:
                n+=1
                break
    return n == len(secret_word)




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    a_str=""
    if letters_guessed==[]:
        a_str="_ "*len(secret_word)
    for char1 in secret_word:
        for char2 in letters_guessed:
            if char1 == char2:
                a_str+=char1
                break
            if char2 == letters_guessed[-1] and char1 != char2:
                a_str+="_ "
    return a_str
    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    a_list=list(string.ascii_lowercase)
    for char in letters_guessed:
            a_list.remove(char)
    return ''.join(a_list)

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    m=6
    #num of guesses
    n=3
    #num of warnings
    vowels="aeiou"  
    unique_letters=[]
    letters_guessed=[]
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("-------------")
    while is_word_guessed(secret_word, letters_guessed)== False:
        print("You have", m, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        please_guess=input("Please guess a letter:")
        if str.isalpha(please_guess)== False:
            if n>0:
                n-=1
                print("Oops! That is not a valid letter. You have", n, "warnings left:", get_guessed_word(secret_word, letters_guessed))    
            else: 
                m-=1
                print("Oops! That is not a valid letter. You have 0 warnings left:", get_guessed_word(secret_word, letters_guessed))
        else: 
            please_guess = str.lower(please_guess)
            if please_guess in letters_guessed:
                if n>0:
                    n-=1
                    print("Oops! You've already guessed that letter. You now have", n, "warnings:", get_guessed_word(secret_word, letters_guessed))    
                else: 
                    m-=1
                    print("Oops! You've already guessed that letter. You now have 0 warnings:", get_guessed_word(secret_word, letters_guessed))    
            else:
                letters_guessed.append(please_guess)
                if please_guess in secret_word:
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                    unique_letters.append(please_guess)
                else:
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))    
                    if please_guess in vowels:
                        m-=2
                    else:
                        m-=1
        if m<=0:
            print("Sorry, you ran out of guesses. The word is", secret_word)
            break
        print('-------------')
    if is_word_guessed(secret_word, letters_guessed)==True:
        print("Congratulations, you won!")
        score = m*len(unique_letters)
        print("Your total score for this game is:", score)

    return ""
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word=get_guessed_word(secret_word, letters_guessed)
    my_word=my_word.replace(' ','')
    if len(my_word)==len(other_word):
        for i in range(len(my_word)):
            if my_word[i]!="_" and my_word[i]!=other_word[i]:
                return False
        return True
    return False
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    for e in wordlist:
        if match_with_gaps(my_word, e)==True:
            print(e)
    return ''




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    m=6
    #num of guesses
    n=3
    #num of warnings
    vowels="aeiou"   
    unique_letters=[]
    
    my_word=get_guessed_word(secret_word, letters_guessed)
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("-------------")
    while is_word_guessed(secret_word, letters_guessed)== False:
        print("You have", m, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        please_guess=input("Please guess a letter:")
        if str.isalpha(please_guess)== False:
            if please_guess=='*':
                print(show_possible_matches(my_word))
            elif n>0:
                n-=1
                print("Oops! That is not a valid letter. You have", n, "warnings left:", get_guessed_word(secret_word, letters_guessed))    
            else: 
                m-=1
                print("Oops! That is not a valid letter. You have 0 warnings left:", get_guessed_word(secret_word, letters_guessed))
        else: 
            please_guess = str.lower(please_guess)
            if please_guess in letters_guessed:
                if n>0:
                    n-=1
                    print("Oops! You've already guessed that letter. You now have", n, "warnings:", get_guessed_word(secret_word, letters_guessed))    
                else: 
                    m-=1
                    print("Oops! You've already guessed that letter. You now have 0 warnings:", get_guessed_word(secret_word, letters_guessed))    
            if not please_guess in letters_guessed:
                letters_guessed.append(please_guess)
                if please_guess in secret_word:
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                    unique_letters.append(please_guess)
                else:
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))    
                    if please_guess in vowels:
                        m-=2
                    else:
                        m-=1
        if m<=0:
            print("Sorry, you ran out of guesses. The word is", secret_word)
            break
        print('-------------')
    if is_word_guessed(secret_word, letters_guessed)==True:
        print("Congratulations, you won!")
        score = m*len(unique_letters)
        print("Your total score for this game is:", score)

    return ""




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
