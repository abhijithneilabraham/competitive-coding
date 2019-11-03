#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:51:13 2019

@author: abhijithneilabraham
"""

def extralongfactorials(n):
    a=1
    for k in range(1,n+1):
        a=a*k
    return a
        
    
        
        
print(extralongfactorials(25))
         
     
    