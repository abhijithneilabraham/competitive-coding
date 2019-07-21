#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 19:04:58 2019

@author: abhijithneilabraham
"""

a=[-1,2,4,-3,5,2,-5,2]
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
        
        
        
        