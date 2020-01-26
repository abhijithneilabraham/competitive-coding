#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 02:03:47 2020

@author: abhijithneilabraham
"""

def evenfib(n):
    a,b,c=0,1,0
    while a<=n:
        a+=b
        if a%2==0:
            c+=a
        a,b=b,a
    return c
        
print(evenfib(4000000))

    