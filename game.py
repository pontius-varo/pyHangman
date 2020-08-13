#Hangman Python
import math
import sys
import time
import random
import functools
##Establish the hangman class
class Hangman:

    ##Add a score
    score = 0
    ##Create an array full of potential words
    words = [ "hat", "constantinople", "hispana", "rome", "arch", "athens",
            "paris", "lima", "guayaquil", "portoviejo", "vienna", "seville",
            "valladolid", "oveido", "porto", "lisbon", "pavia", "aquileia"]
    ##Wrong letters go below
    wrong_letters = []
    ##Correct letters go below
    correct_letters = []
    ##Initialize object with the following parameters: self (ie. Hangman, & name)
    def __init__(self, nm):
        ##Store the given name into a variable
        self.name = nm
        ##Fetches a random word from the static array 'words'
        word = random.choice(self.words)
        ##Split said word into seperate strings
        self.secretword = self.split(word)
        print(self.secretword)
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

    ##Game state in which the player will provide inputs that will match the strings or not
    def Gamestate(self):

       #Figure out how to display the used letters array!
        while True:

            userletter = input('Enter a letter: ')

            if (userletter not in self.wrong_letters):

                if userletter in self.secretword:
                    print("That is correct.")
                    self.correct_letters.append(userletter)
                    print (self.correct_letters)
                else:
                    print("That is incorrect")
                    self.wrong_letters.append(userletter)

            if len(self.correct_letters) == len(self.secretword):
                self.Game_over(0)
                return

            if len(self.wrong_letters) == 6:
                self.Game_over(1)
                return

    def Game_over(self, x):

        while True:

            if x ==  1:
                print('You lose!')
            else:
                print('You win!')

            option = input('Play again? >>> ')

            if option == 'yes':
                self.Pregame()
            elif option == 'no':
                quit()
            else:
                print('I don\'t know what that means!')


    def split(self, word):
        return [char for char in word]

    def sub(x, y):
        x = x - y
        return x



## Initialize pygame
#pygame.init()


##Initialize Game itself
#Figure out how to prompt the user inside the pygame window!
name = input("Please enter your name >>> ")

start = Hangman(name)
