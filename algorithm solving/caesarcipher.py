#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:16:12 2019

@author: abhijithneilabraham
"""

def caesarCipher(s, k):
    l=""
    for i in s:
        if i.isupper():
            l+=chr((ord(i)+k-65)%26+65)
        elif i.islower():
            l+=chr((ord(i)+k-97)%26+97)
        else:
            l+=i
        
            
    print(l)
    return l
caesarCipher("middle-Outz-",2)

        
        
    
    
    
