#Hangman Python
import functools
import random
from itertools import repeat
from lib import graphics

class Hangman:

    ##Add a score
    score = 0
    ##Create an array full of potential words
    words = [ "hat", "constantinople", "hispana", "rome", "arch", "athens",
            "paris", "lima", "guayaquil", "portoviejo", "vienna", "seville",
            "valladolid", "oveido", "porto", "lisbon", "pavia", "aquileia"]
    ##Wrong letters go belo
    wrong_letters = []
    ##Correct letters go below
    correct_letters = []
    ##Initialize object with the following parameters: self (ie. Hangman, & name)
    def __init__(self, nm):
        ##Store the given name into a variable
        self.name = nm
        ##Fetches a random word from the static array 'words'
        word = random.choice(self.words)
        self.secretword = str(word)
        ##Start the pregame
        self.Pregame()

    ##Pre-game state in which the user is given the option to begin or exit.
    def Pregame(self):
        print ("Hello, " + self.name + "!", "Time to play hangman!")
        print ("Enter 'start' to begin. Otherwise, enter 'exit'")

    ##A while loop to wait until the user decides to start the game or not.
        while True:
            via = input(">>> ")

            if via == 'start':
                self.Gamestate()
            elif via == 'exit':
                quit()
            else:
                print('I don\'t understand what that means')

    # The following was borrowed mostly from https://github.com/aglla/pyprojects/blob/master/hangman.py
    def display(self, HANGMANPICS):
        print(self.name)
        print(self.score)
        print(HANGMANPICS[len(self.wrong_letters)])
        hidden = "_" * len(self.secretword)
        currentword = self.secretword

        for x in range(0, len(self.secretword)):
            if self.secretword[x] not in self.correct_letters:
                currentword = currentword.replace(self.secretword[x], '_')
        print(currentword)

    def Gamestate(self):

        while True:

            self.display(graphics.HANGMANPICS)
            userletter= str(input('Enter a letter: '))

            if len(userletter) != 1:
                print('Invalid Character!')

            if (userletter in self.wrong_letters) or (userletter in self.correct_letters):
                print('You already guessed that dofus!')

            elif userletter in self.secretword:
                print("That is correct")
                cnt = self.secretword.count(userletter)
                self.correct_letters.extend(repeat(userletter, cnt))
                self.score += 1
            else:
                print("That is incorrect")
                self.wrong_letters.append(userletter)
                self.score -= 1
            if len(self.correct_letters) == len(self.secretword):
                self.Game_over(0)

            if len(self.wrong_letters) == 6:
                self.Game_over(1)

    def Game_over(self, x):

        while True:

            if x == 1:
                print('You lose! The correct word was', self.secretword)
                quit()
            else:
                print('You win! The word was', self.secretword)
                quit()
            #option = input('Play again?(y/n) >>> ')

            #if option == 'y':
                #reset()
            #elif option == 'n':
                #quit()
            #else:
                #print('I don\'t know what that means!')

name = input("Please enter your name >>> ")
start = Hangman(name)
