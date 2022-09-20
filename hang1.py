
import sys
import random
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]
category = "Państwa"
words = 'AFGANISTAN ALBANIA BELGIA RUMUNIA'.split()





def main():

    missed_letters = []
    correct_letters = []
    secret_word = random.choice(words)

    while True:
        drawHangman (missed_letters, correct_letters, secret_word)

        guess = getPlayerGuess (missed_letters + correct_letters)
        if guess in secret_word:
            correct_letters.append(guess)

            found_all_letters = True
            for secret_word_letter in secret_word:
                if secret_word_letter not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                print("Ukryte słowo to:" , secret_word)
                print ("Wygrałeś")
                break


        else:
            missed_letters.append(guess)
            if len(missed_letters) == len(HANGMAN_PICS) -1:
                drawHangman (missed_letters, correct_letters, secret_word)
                print("Wykorzystałeś już wszystkie szanse")
                print ("Ukryte słowo to:", secret_word)
                break

def drawHangman (missed_letters, correct_letters, secret_word):
    print (HANGMAN_PICS [len(missed_letters)])
    print ("Kategoria ukrytego słowa to:", category)
    print()
    print("Błędne litery: ", end ='')
    for letter in missed_letters:
        print (letter, end = ' ')
    if len(missed_letters) == 0:
        print ("Nie podałeś jeszcze błędnej litery")
    print() 

    blanks = ["_"] *len(secret_word)

    for i in range (len(secret_word)): 
        if secret_word[i] in correct_letters:
            blanks [i] = secret_word[i]
    print (' ' .join(blanks))


def getPlayerGuess (alreadyGuessed):
    while True:
        print ("Podaj literę")
        guess = input('>').upper()
        if len(guess) != 1:
            print("Proszę podaj tylko jedną literę.")
        elif guess in alreadyGuessed:
            print ("Tą literę już podawałeś")
        elif not guess.isalpha():
            print ("Proszę podać LITERĘ")
        else:
            return guess 
            
    
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
