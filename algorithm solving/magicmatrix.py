#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 22:27:23 2019

@author: abhijithneilabraham
"""
a=[[4,9,2],[3,5,7],[8,1,5]]
def magicsquare(a):
    k=0
    b=0
    c=0
    for i in range(3):
        k=sum(a[i])
       # print(k)
        if k!=c:
            diff=abs(k-c)
        print(diff)
        c=k 
        
    
    for j in range(3):
        l=0
        for m in range(3):
            l+=a[m][j]
       # print(l)
    for n in range(3):
         b+=a[n][n]
    #print(b)
    
        
        
magicsquare(a)
