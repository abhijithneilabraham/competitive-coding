#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 03:50:09 2020

@author: abhijithneilabraham
"""

def minion_game(string):
    vowels=['A','E','I','O','U']
    k=0
    s=0
    for i in range(len(string)):
        
        if string[i] in vowels:
            k+=len(string)-i

        else:
            s+=len(string)-i
    if s>k:
        print("Stuart",s)
    elif k>s:
        print("Kevin",k)
    else:
        print("Draw")
    
            

minion_game("BANANA")