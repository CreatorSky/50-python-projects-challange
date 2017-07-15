# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 11:56:56 2017

@author: creatorsky

facebook.com/icreatorsky
"""

from random import randint

num = randint(0,101)
guessed = False
count = 0

while guessed is not True:
    if count == 0 :
        print("I've guess a number between 0 to 100. Try to guess the same number. I'll tell you to go High/Low.")
        print("Alright! I've selected a number.")
        count+=1
        continue
    else:
        guess = int(input("Enter your guess : "))
        if guess == num:
            print("Congratulations! You've guessed it.")
            if str(input("Wanna play again? (yes/no): ")).lower() == "yes":
                print("\nOkay then, I've selected one more number.")
                num = randint(0,101)
                continue
            else:
                guessed = True
        else:
            if guess > num:
                print("Go Lower..")
                continue
            else:
                print("Go Higher..")
                continue
                
            
                
        
