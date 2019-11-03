#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 19:04:58 2019

@author: abhijithneilabraham
"""

a=[-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
def maxSubsetSum(a):
    maxsum=0
    c=[]
    i=0
    while i<len(a):
        maxsum+=a[i]
        c.append(maxsum)
        i+=1
    print(c.index(max(c)))
    s=c.index(max(c))
    sum2=0
    sum3=0
    for j in range(s+1):
        sum2+=a[j]
        if sum2>=s:
            sum3=sum2
    print(sum3)
    return sum3
maxSubsetSum(a)
#I guess this one went wrong
        
        
        
        