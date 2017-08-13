# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 14:29:32 2017

@author: creatorsky

facebook.com/icreatorsky
"""

from math import pow
from winsound import Beep
from time import sleep
info = "program convers octave/pitchclass pairs into appropriate Hertz values, using tempered scale conversion."

#print(info)

y = ''

def get_freq(a,b):
    o = a-4
    m = b-9
    freq = 440 * pow(2,(o+(m/12)))
    return int(freq)
'''
while y.lower()!='no':
    octave = int(input("Enter octave :"))
    pitch = int(input("Enter pitch :"))
    freq = get_freq(octave,pitch)
    print(octave,".",pitch,"equals",freq)
    Beep(int(freq),500)
    y = input("\nWanna try again?")
'''

inp = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
out = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
band = dict(zip(inp,out))
st = "E-E---E---C--E---G------dG-----C----dG----dE----dA--dB---dA#--dA-----dG--E---G--A---F--G---E---C--D--dB"



for x in st.split('-'):
    if x == '':
        sleep(0.15)
        continue
    octa = 5
    note = x
    print(x)
    if x[0]=='d':
        octa -= 1
        note = x[1:]
    
    if x[0]=='u':
        octa +=1
        note = x[1:]
    Beep(get_freq(octa,band[note]),275)
    octa = 3








