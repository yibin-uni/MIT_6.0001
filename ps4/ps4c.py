# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)

    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text


    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words
    
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        transpose_dict={}
        upper_vowels_perm=str.upper(vowels_permutation)
        all_letters=string.ascii_letters
        for char in all_letters:
            transpose_dict[char]=char
        for i in range(len(VOWELS_LOWER)):
            transpose_dict[VOWELS_LOWER[i]]=vowels_permutation[i]
            transpose_dict[VOWELS_UPPER[i]]=upper_vowels_perm[i]
        return transpose_dict

    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        message_text=SubMessage.get_message_text(self) #这一行需要吗？
        new_message_list=list(message_text)
        for i in range(len(message_text)):
            char=message_text[i]
            if str.isalpha(char)==True:
                new_message_list[i]=transpose_dict[char]
        new_message=''.join(new_message_list)
        return new_message

        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)


    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        message_text=SubMessage.get_message_text(self)
        all_perm=get_permutations(VOWELS_LOWER)
        word_list=SubMessage.get_valid_words(self)
        dec_dict={}
        n=0 #valid count
        num=0 #current largest valid count
        best=''
        for e in all_perm:
            enc_dict=SubMessage.build_transpose_dict(self,e)
            dec_dict={v:k for k,v in enc_dict.items()}
#            tran_keys=list(enc_dict.keys())
#            tran_values=list(enc_dict.values())
#            for i in range(len(tran_keys)):
#                dec_dict[tran_values[i]]=tran_keys[i]  #反向字典
            dec_message=SubMessage.apply_transpose(self, dec_dict)
            dec_message_list=dec_message.split()
            for f in dec_message_list:
                if is_word(word_list, f)==True:
                    n+=1
            if n>num:
                num=n
                best=dec_message
            n=0
        if num==0:
            return message_text
        return best


if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    my_mes_1= SubMessage('On behalf of Blizzard Entertainment, I wish all Chinese players a happy lunar new year!')  
    perm_1='oiaeu'
    enc_dict_1= my_mes_1.build_transpose_dict(perm_1)
    print('Original message:', my_mes_1.get_message_text(), 'Permutation:', perm_1)
    print('Expected encryption:', 'En biholf ef Blazzord Intirtoanmint, A wash oll Chanisi ployirs o hoppy lunor niw yior!')  
    print('Actual encryption:', my_mes_1.apply_transpose(enc_dict_1))
    enc_message_1= EncryptedSubMessage(my_mes_1.apply_transpose(enc_dict_1))
    print('Decrypted message:', enc_message_1.decrypt_message())
#写一个return original text的
    my_mes_2= SubMessage('lutwatz corqlm golamtiprituy')
    perm_2='uaeio'
    enc_dict_2=my_mes_2.build_transpose_dict(perm_2)
    print('Original message:', my_mes_2.get_message_text(), 'Permutation:', perm_2)
    print('Expected encryption:', 'lotwutz cirqlm gilumtepretoy')  
    print('Actual encryption:', my_mes_2.apply_transpose(enc_dict_2))
    enc_message_2= EncryptedSubMessage(my_mes_2.apply_transpose(enc_dict_2))
    print('Decrypted message:', enc_message_2.decrypt_message())
