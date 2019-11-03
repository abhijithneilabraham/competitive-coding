#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:46:30 2019

@author: abhijithneilabraham
"""

def pageCount(n, p):
    if int(n) in range(1,100001): 
        if n%2==0 and p>=5:
            arr=[abs(p-n)+1,p]
            return abs(min(arr))//2
        else:
            arr=[abs(p-n),p,n]
            return abs(min(arr))//2
    else:
        return False
        
n=int(input())
p=int(input())
print(pageCount(n,p))