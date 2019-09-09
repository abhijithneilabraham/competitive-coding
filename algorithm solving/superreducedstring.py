#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 01:48:28 2019

@author: abhijithneilabraham
"""

def superReducedString(s):
    i=0
    n=len(s)
    while i<n:
        
        if s[i]==s[i-1]:
            s=s.replace(s[i]+s[i-1],"")
            n=len(s)
            i=0
        
        i+=1
    if len(s)==0:
        print("Empty String")
        return "Empty String"
    else:
        print(s)
        return s
        
    
superReducedString("baab")