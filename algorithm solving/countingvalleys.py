#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 23:33:32 2020

@author: abhijithneilabraham
"""

def countingValleys(n, s):
    c=0
    d=0
    for i in range(len(s)):
        if s[i] in 'U':
            c+=1
        else:
            c-=1
        if c==-1 and s[i] not in 'U':
            d+=1
    return d
    