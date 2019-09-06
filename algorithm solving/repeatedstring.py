#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 02:59:05 2019

@author: abhijithneilabraham
"""
a="aba"
def repeatedString(s, n):
    m=s.count('a')
    ct=m*(n//len(s))
    mod=n%len(s)
    for i in range(mod):
        if s[i]=="a":
            ct+=1
    print(ct)
    
repeatedString(a,10)