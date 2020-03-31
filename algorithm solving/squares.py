#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 03:51:28 2020

@author: abhijithneilabraham
"""
def squares(a, b):
    rt1=int(a**(1/2))
    rt2=int(b**(1/2))
    a=[i**2 for i in range(rt1,rt2+2) if i**2>=a and i**2<=b]
    return len(a)
print(squares(3,9))
            
