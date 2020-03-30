#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 02:01:02 2020

@author: abhijithneilabraham
"""

def appendAndDelete(s, t, k):
   
    if s==t:
        print("Yes")
        return "Yes"
    for i in range(len(s)):
        s=s[:-1]
        k-=1
        print(s,k)
        if s in t :
            if s+t[-k:]==t and k>=0:
                print("Yes")
                return "Yes"

    print("No")
    return "No"
            
        
        

appendAndDelete("asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv","bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv",100)