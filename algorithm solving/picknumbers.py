#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 01:37:13 2019

@author: abhijithneilabraham
"""
a=[4,3,6,5,3,3,1]

def pickingNumbers(a):
    b=list(set(a))
    c=[]
    for i in range(len(b)):
        if b[i]-b[i-1]==1:
            c.append(a.count(b[i])+a.count(b[i-1]))
        elif b[i]-b[i-1]==0:
            c.append(a.count(b[i]))
    print(max(c))
    return max(c)
        
            
            
    
pickingNumbers(a)
    