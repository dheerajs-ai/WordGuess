"""
File: word_guess.py
-------------------
Fill in this comment.
"""
import random
from PIL import Image
LEXICON_FILE = "Lexicon.txt"    # File to read word list from


def play_game(secret_word):
    empty= ['_']*len(secret_word)
    guesses = 8                                                                 #Initial number of guesses for player
    gs=guesses
    print('There are ' + str(guesses) + ' chances left.')
    while (guesses>0):
        guess = input('Enter your guess:').strip().upper()                      #prompt for guess
        while len(guess)!=1:
            guess = input('Enter your guess:').strip().upper()
        if  guess in secret_word and guess not in empty:                        #eligible guess
            pos= guessp(secret_word, guess)
            for j in pos:
                empty[j]= guess
            print(''.join(empty))
        elif guess not in secret_word:                                           #wrong guess
            guesses-=1
            print('There are ' + str(guesses) + ' chances left.')
        else:
            print('Already exists!')
            print('There are ' + str(guesses) + ' left.')
        if ''.join(empty) == secret_word:
            print('You guessed it right')
            print('You made it in ' + str(gs-guesses) + ' chances' )
            img = Image.open('fyt99vlvchm31.jpg')
            img.show()
            return

    img = Image.open('unnamed.png')
    img.show()
    return


def guessp(secret_word, guess):
    lis=[]
    for j in range(len(secret_word)):                           #sorting out index value of alphabet in word
        if guess == secret_word[j]:
            lis.append(j)
    return lis

def get_word():

    file = open('Lexicon.txt')                                  #opens up text file
    list = []                                                   #created an empty list to store words
    for line in file:                                           #storing values in list
        line.strip()
        list.append(line.strip())
    max = len(list)                                             
    chosen_no = random.randrange(max)                           #chosing random index value from the list of words
    chosen_random = list[chosen_no]
    return chosen_random                                        #gives back our secret word


def main():
    secret_word = get_word()                                    #ask machine for a random word
    print(secret_word)                                              #lets cheat
    print('_ ' * len(secret_word))                              #print dashes for the number to be guessed
    play_game(secret_word)                                      #where shit happens

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()