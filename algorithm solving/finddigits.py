#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:53:42 2020

@author: abhijithneilabraham
"""

def findDigits(n):
    n=str(n)
    c=0
    for i in n:
        i=int(i)
        n=int(n)
        if i==0:
            continue
        elif n%i==0:
            c+=1
            
    print(c)
    return c
findDigits(1012)
    