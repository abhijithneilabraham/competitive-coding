#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:41:29 2019

@author: abhijithneilabraham
"""

def pangrams(s):
    s=list(s)   
    d=[i for i in range(97,123)]
    for i in s:
        i=i.lower()
        if ord(i) in d:
            d.remove(ord(i))
    if len(d)==0:
        print("pangram")
        return "pangram"
    else:
        print("not pangram")
        return "not pangram"
pangrams("We promptly judged antique ivory buckles for the prize")            