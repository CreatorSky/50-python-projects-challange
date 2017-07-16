# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 14:12:06 2017

@author: creatorsky

facebook.com/icreatorsky
"""

import random

hangman = [
        
        '''
        +-----+
        |     |
              |
              |
              |
              |
              |
              |
    ============
        
        ''',
        
        '''
        +-----+
        |     |
        O     |
              |
              |
              |
              |
              |
    ============
        
        ''',
        
        '''
        +-----+
        |     |
        O     |
        |     |
              |
              |
              |
              |
    ============
        
        ''',
        
        '''
        +-----+
        |     |
        O     |
       /|     |
              |
              |
              |
              |
    ============
        
        ''',
        
        '''
        +-----+
        |     |
        O     |
       /|\    |
              |
              |
              |
              |
    ============
        
        ''',
        
        '''
        +-----+
        |     |
        O     |
       /|\    |
       /      |
              |
              |
              |
    ============
        
        ''',
        
        '''
        +-----+
        |     |
        O     |
       /|\    |
       / \    |
              |
              |
              |
    ============
        
        ''',
        
        
        ]

words = ['accidental', 'alcoholic', 'amuse', 'amusing', 'animal', 'appliance', 'argument', 'art', 
         'babies', 'berry', 'bouncy', 'box', 'brainy', 'broken', 
         'cause', 'charming', 'classy', 'clever', 'clip', 'coal', 'coil', 'comb', 'complain', 'crack', 'cracker', 'crowd', 
         'daffy', 'dramatic', 'efficient', 'example', 'eyes', 
         'faithful', 'feeble', 'flood', 'force', 'forgetful', 'fruit', 'fuel', 'furniture', 
         'gentle', 'grade', 'guttural', 'habitual', 'helpful', 
         'hope', 'horn', 'hypnotic', 'idea', 'impress', 
         'instrument', 'iron', 
         'jail', 'jeans', 'judge', 
         'label', 'lavish', 'long', 
         'minister', 'mint', 'moaning', 
         'nice', 'numberless', 
         'obtainable', 
         'peaceful', 'perfect', 'poke', 'political', 'private', 
         'ratty', 'real', 'rely', 'roomy', 'rough', 
         'saw', 'scare', 'school', 'screw', 'scrub', 'shiny', 'short', 'shrug', 'silly', 'snotty', 'sort', 'spark', 'special', 'stem', 'stew', 'subtract', 'summer', 
         'tasteful', 'trick', 'twist', 
         'unarmed', 'unique', 'unkempt', 
         'waste', 'weight', 'wish', 
         'zinc']


def get_word():
    n = random.randint(0,100)
    return words[n]

def hide(word):
    a = ''
    for _ in range(len(word)):
        a += '_ '
    return a

def printh(count,_,guess='',miss=[]):
    print(hangman[count], "\nWord  :",_, "\nGuess :",guess, "\nMiss  :",','.join(x for x in miss))


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


    
    
def main(): 
    count = 0
    miss = []
    mark = ""
    word = get_word()
    _ = hide(word)
    while True:
        if count == 0:
            print("You'll have to guess the word. Length of the word is",len(word))
            printh(count,_)
        inp = str(input("Enter guess : ")).lower()
        if inp in word:
            ind = find(word,inp)
            for x in ind:
                temp_list = _.split(' ')
                temp_list[x] = inp
                mark = ''.join(temp_list)
                _ = ' '.join(temp_list)
        else:
            miss.append(inp)
            count += 1
            
        printh(count,_,inp,miss)
        if mark == word :
            print("Congratulations ! You successfully guessed the word",word)
            break
        if count == 6:
            print("\nGame Over. The word was",word)
            break
            
    

main()
        
    


























