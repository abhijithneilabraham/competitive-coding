#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:57:27 2019

@author: abhijithneilabraham
"""

def alternate(s):
    p=[0]*len(s)
    i=1
    while i<len(s):
        if s[i]==s[i-1]:
            s=s.replace(str(s[i]),"")        
        i+=1
    b=0
    for j in range(2):
        a=max(set(s),key=s.count)
        b+=s.count(a)
        s=s.replace(a,"")
       
    print(b)
    return b
alternate("beabeefeab")
            
            