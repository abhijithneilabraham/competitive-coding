#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 04:00:39 2019

@author: abhijithneilabraham
"""

def hackerrankInString(s):
    h="hackerrank"
    c=0
    for i in range(len(s)):
        if h[c]==s[i]:
            c+=1
            if c==len(h):
                print("YES")
                return "YES"
    print("NO")
    return "NO"
hackerrankInString("rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt")
                    
            
        