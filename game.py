#Hangman Python
import math
import sys
import time
import random

class Hangman:
 
    words = [ "hat", "constantinople", "hispana", "rome", "arch", "athens",
            "paris", "lima", "guayaquil", "portoviejo", "vienna", "seville",
            "valladolid", "oveido", "porto", "lisbon", "pavia", "aquileia"]
    
    # Not sure if an alphabet is necessary
    alphabet = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
            "x", "y", "z"]
    
    Num_guesses = 7

    def __init__(self, nm):
        
        self.name = nm
        
        word = random.choice(Hangman.words) 
        secretword = word.splitlines()
        
        #print(secretword)

    def Greeting(self):
    
        print ("Hello, " + self.name + "!", "Time to play hangman!")
        print ("Enter 'start' to begin. Otherwise, enter 'exit'")
        via = input(">>> ")
        
        if via == 'start':
            Hangman.Gamestate()
        elif via == 'exit':
            quit()
        else:
            print('I don\'t understand what that means')

    def Gamestate(self):
         
        time.sleep(1)
        print('Take a guess.....')
        time.sleep(0.5)

        while Num_guesses < 7:

            pass


name = input("Please enter your name >>> ")

start = Hangman(name)    
start.Greeting()    
