#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:46:30 2019

@author: abhijithneilabraham
"""

def pageCount(n, p):
    count=0
    if n%2==0 and n<p:
    
        for i in range(n,p,2):
            count+=1
    elif n%2==0 and n>p:
        for i in range(p,n,2):
            count+=1
    elif n%2!=0 and n<p:
        n-=1
        for i in range(n,p,2):
            count+=1
    elif n%2!=0 and n>p:
        n=n-1
        for i in range(p,n,2):
            count=count+1
    elif n==p:
        count =0
    return count-1
    
n=int(input())
p=int(input())
print(pageCount(n,p))