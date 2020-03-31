#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 03:51:28 2020

@author: abhijithneilabraham
"""
def squares(a, b):

    c=len([i**2 for i in range(int(a**(1/2)),int(b**(1/2))+2) if i**2>=a and i**2<=b])
    return c
print(squares(1,200000))
            
