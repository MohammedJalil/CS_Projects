# File: Project2.py
# Student: Mohammed Jalil
# UT EID: mhj476
# Course Name: CS303E
# 
# Date Created: 4/10/21
# Date Last Modified: 4/12/21
# Description of Program: This program allows for the implementation of a
# substitution cipher that will generate a random key at the beginning.
# The user can choose to see what the key is and change the key (manually or
# randomly). The program can also encrypt and decrypt text inputted by the
# user using the cipher and a quit input will leave the program.

import random

# A global constant defining the alphabet. 
LCLETTERS = "abcdefghijklmnopqrstuvwxyz"

# You are welcome to use the following two auxiliary functions, or 
# define your own.   You don't need to understand this code at this
# point in the semester. 

def isLegalKey( key ):
    # A key is legal if it has length 26 and contains all letters.
    # from LCLETTERS.
    return ( len(key) == 26 and all( [ ch in key for ch in LCLETTERS ] ) )

def makeRandomKey():
    # A legal random key is a permutation of LCLETTERS.
    lst = list( LCLETTERS )  # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    return ''.join( lst )    # Assemble them back into a string

def encryptText():
    pass

def decrpytText():
    pass
        
        

# There may be some additional auxiliary functions defined here.
# I had several others, mainly used in encrypt and decrypt. 

class SubstitutionCipher:
    def __init__ (self, key = makeRandomKey() ):
        """Create an instance of the cipher with stored key, which
        defaults to random."""
        self.__key = key

    # Note that these are the required methods, but you may define
    # additional methods if you need them.  (I didn't need any.)

    def getKey( self ):
        """Getter for the stored key."""
        return self.__key

    def setKey( self, newKey ):
        """Setter for the stored key.  Check that it's a legal
        key."""
        if isLegalKey(newKey) is False:
            print("Key entered is not legal")
        else:
            self.__key = newKey

    def encryptText( self, plaintext ):
        """Return the plaintext encrypted with respect to the stored key."""

    def decryptText( self, ciphertext ):
        """Return the ciphertext decrypted with respect to the stored
        key."""

def main():
    """ This implements the top level command loop.  It
    creates an instance of the SubstitutionCipher class and allows the user
    to invoke within a loop the following commands: getKey, changeKey,
    encrypt, decrypt, quit."""

    cipher = SubstitutionCipher()
    
    while (True):
        mode = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")

        if mode.lower() == "getkey":
            print("  Current cipher key: ", cipher.getKey())

        elif mode.lower() == "changekey":
            while (True):
                changedKeyMode = input("  Enter a valid cipher key, 'random' for a " \
                                       "random key, or 'quit' to quit: ")
                if changedKeyMode == "random":
                    cipher.setKey(makeRandomKey())
                    print("    New cipher key: ", cipher.getKey())
                    break
                elif changedKeyMode == "quit":
                    break
                else:
                    if isLegalKey(changedKeyMode) is True:
                        print("    New cipher key: ", cipher.getKey())
                    else:
                        print("    Illegal key entered. Try again!")

        elif mode.lower() == "encrypt":
            encryptMode = input("  Enter a text to encrypt: ")
            for i in plainText:
                place = encryptMode.find(i)

            print("    The encrypted text is: ", encryptText(cipher.getKey()))

        elif mode.lower() == "decrypt":
            decryptMode = input("  Enter a text to decrypt: ")
            for i in decryptMode:
                place = decryptMode.find(i)
                
            print("    The decrypted text is: ", decryptText(cipher.getKey()))

        elif mode.lower() == "quit":
            print("Thanks for visiting!")
            return
            

main()
