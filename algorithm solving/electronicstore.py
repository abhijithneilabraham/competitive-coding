#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 01:34:07 2019

@author: abhijithneilabraham
"""
k=[3,1]

def getMoneySpent(k, d, b):
    k=sorted(k)
    k=k[::-1]
    d=sorted(d)
    d=d[::-1]
    c=[]
    for i in range((len(k))):
        for j in range(len(d)):
            diff=k[i]+d[j]
            if diff<=b:
                c.append(diff)
    
    if len(c)!=0:
        print(max(c))
        return max(c)        
    else:
        print("-1")
        return str(-1)
            
getMoneySpent(10,2,3)
        
a=[1,2,3]
print(a[::-1])
    
    