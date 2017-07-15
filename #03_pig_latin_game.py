# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 13:10:59 2017

@author: creatorsky

facebook.com/icreatorsky
"""


#For info search wiki : Pig latin game

word = str(input("Enter Word : ")).lower()

vow = ['a','e','i','o','u']

for x in word:
    if word.index(x)==0 and x in vow:
        print(word+"ay")
        break
    elif x in vow and word.index(x)!=0:
        front = word[:word.index(x)]
        print(word[word.index(x):]+front+"ay")
        break