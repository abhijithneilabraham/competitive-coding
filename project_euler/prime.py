#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:31:59 2020

@author: abhijithneilabraham
"""

def lprime(n):
    
    k=[i for i in range(2,n//2) if n%i==0]
    l=n
    for i in range(n//2,2,-1):
        if n%i==0:
            for j in k:
                if i%j!=0 and i>j:
                    l=i
                    print(i,j)
            
            
    return l
    

        
print(lprime(6008514))