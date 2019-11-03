#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 23:12:13 2019

@author: abhijithneilabraham
"""
a=[3,9,6]
b=[36,72]
def getTotalX(a, b):
    c=max(b)
    flag=0
    count=0
    for j in range(c):
        for i in a:
            if j%i==0:
                flag=1
            else:
                flag==0
                break
        if flag==1 :
            count+=1
    print(count)
            
        
            
            
getTotalX(a,b)
                
            
    