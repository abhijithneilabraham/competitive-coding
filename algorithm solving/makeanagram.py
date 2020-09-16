#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:16:17 2020

@author: abhijithneilabraham
"""

def makeAnagram(a, b):
    c=0
    for i in set(a+b):
        if i in a and i in b:
            c+=abs(a.count(i)-b.count(i))
        else:
            c+=a.count(i)+b.count(i)
    

    return c
