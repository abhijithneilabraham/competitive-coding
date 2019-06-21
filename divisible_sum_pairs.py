#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 01:18:30 2019

@author: abhijithneilabraham
"""
arr=[1,3,2,6,1,2]
n=6
k=3
def divisibleSumPairs(n, k, arr):
    count=0
    for i in range(len(arr)):
        n=arr[i]%k
        if n!=0 :
            for j in range(len(arr)):
                if n==j and j!=i:
                    count=count+1
    return count
                    
print(divisibleSumPairs(n,k,arr))
            
        