#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 17:15:18 2019

@author: abhijithneilabraham
"""
arr='UDDDUDUU'

def countingValleys(n, s):
    level=0
    valley=0
    for i in range(n):
        if s[i]=='U':
            level+=1
        elif s[i]=='D':
            level-=1
            
        if level<0 and s[i] =='U' :
            valley+=1
    return valley        
print(countingValleys(8,arr))