#Hangman Python
import math
import sys
import time
import random

##Establish the hangman class
class Hangman:
    
    ##Create an array full of potential words
    words = [ "hat", "constantinople", "hispana", "rome", "arch", "athens",
            "paris", "lima", "guayaquil", "portoviejo", "vienna", "seville",
            "valladolid", "oveido", "porto", "lisbon", "pavia", "aquileia"]
    
    ##Not sure if an alphabet is necessary
    alphabet = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
            "x", "y", "z"]
    
    Num_guesses = 7
    
    ##Initialize object with the following parameters: self (ie. Hangman, & name)
    def __init__(self, nm):
        ##Store the given name into a variable
        self.name = nm
        ##Fetches a random word from the static array 'words' 
        word = random.choice(self.words)
        ##Split said word into seperate strings
        secretword = self.split(word)
        print(secretword)
        ##Start the pregame
        self.Greeting()
    
    ##Pre-game state in which the user is given the option to begin or exit.
    def Greeting(self):
    
        print ("Hello, " + self.name + "!", "Time to play hangman!")
        print ("Enter 'start' to begin. Otherwise, enter 'exit'")
        via = input(">>> ")
        
        if via == 'start':
            self.Gamestate()
        elif via == 'exit':
            quit()
        else:
            print('I don\'t understand what that means')
            return 
    
    ##Game state in which the player will provide inputs that will match the strings or not
    def Gamestate(self):
         
        time.sleep(1)
        print('Take a guess.....')
        time.sleep(0.5)

        while self.Num_guesses < 7:

            pass
    
    def split(self, word):
        return [char for char in word]

name = input("Please enter your name >>> ")

start = Hangman(name)        
