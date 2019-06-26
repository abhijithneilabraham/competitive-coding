#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 23:12:13 2019

@author: abhijithneilabraham
"""
a=[3,9,6]
b=[36,72]
def getTotalX(a, b):
    count=0
    for i in a:
        for j in b:
            if j>i and j%i==0 :
                count+=1
            
    print(count//2)
    return count//2
getTotalX(a,b)
                
            
    