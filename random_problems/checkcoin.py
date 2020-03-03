#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 00:20:23 2020

@author: abhijithneilabraham
"""

l=0

def getWays(n, c):
    global l
    if n==0:
        return 0
    for i in range(len(c)):
        if c[i]<=n:
            l+=1
            getWays(n-c[i],c)
            
            return l
            
            
print(getWays(4,[1,2,3]))