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
            
            
print(getWays(166,[5 ,37 ,8 ,39 ,33 ,17 ,22 ,32 ,13 ,7 ,10 ,35 ,40 ,2 ,43 ,49 ,46 ,19 ,41 ,1 ,12 ,11 ,28]))