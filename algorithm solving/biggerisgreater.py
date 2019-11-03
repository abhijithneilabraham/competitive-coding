#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:24:04 2019

@author: abhijithneilabraham
"""

def biggerIsGreater(w):
    if len(set(w))==1:
        print("no answer")
        return "no answer"
    else:
        a=[ord(i) for i in w]
        if a[1]==max(a):
            a=a[2:]+a[:2]
        else:
            z=sorted(a)
            z=z[::-1]
            #print(a)
            #print(z)
            for i in range(len(a)):
                if a[i]-z[i]>0:
                    a[i-1],a[i]=a[i],a[i-1]
                    break
    
            #print(a)
        c=[chr(i) for i in a]
        b=""
        b=b.join(c)
        print(b)
        return b
biggerIsGreater("dkhc")