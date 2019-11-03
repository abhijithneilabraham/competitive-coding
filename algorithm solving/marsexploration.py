#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 04:27:31 2019

@author: abhijithneilabraham
"""

def marsExploration(s):
    i=2
    c=0
    while i<=len(s):
        d=s[i-2]+s[i-1]+s[i]
        if d[0]!="S":
            c+=1
        if d[1]!="O":
            c+=1
        if d[2]!="S":
            c+=1
        i=i+3
    print(c)
    return c
marsExploration("SOSOOSOSOSOSOSSOSOSOSOSOSOS")
