#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 23:10:34 2020

@author: abhijithneilabraham
"""

def sieveoferatosthenes(n): 
    half=(n//2)+1
    p=2
    prime=[True for i in range(half)]
    while(p*p<=n//2):
        if prime[p]:
            for i in range(p*p,half,p):
                prime[i]=False


        p+=1
    l=n
    for i in range(2,half):
        if prime[i] and n%i==0:
            l=i
    return l
#        
        
                
print(sieveoferatosthenes(33))
    