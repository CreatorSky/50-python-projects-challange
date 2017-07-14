# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 20:27:11 2017

@author: creatorsky

facebook.com/icreatorsky
"""

import requests
from time import sleep
import sys
from bs4 import BeautifulSoup

def convert(amount,frm,to):
    url = "https://www.google.com/finance/converter?a="+str(amount)+"&from="+frm.upper()+"&to="+to.upper()
    print("Converting...")
    #result = requests.get(url)
    #soup = BeautifulSoup(requests.get(url).content, "lxml")
    ress = BeautifulSoup(requests.get(url).content, "lxml").find('span', {'class':'bld'})
    if ress is not None:
        print(amount, frm, " = " , ress.string.strip())
    else:
        print("invalid currency. Reffer these codes :")
        sleep(1)
        select = BeautifulSoup(requests.get(url).content, "lxml").find('select', {'name':'from'})
        options = select.findChildren()
        for option in options:
            print(option.string.strip(), " : ", option.attrs['value'])
        print("\n\n")
        main()
    

def main():
    print("example: From : usd   To:inr")
    amount = float(input("Enter Amount : "))
    frm = str(input("From : "))
    to = str(input("To : "))
    convert(amount,frm,to)
    
main()    
