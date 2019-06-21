#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 01:18:30 2019

@author: abhijithneilabraham
"""
arr=[5,9,10,7,4]

n=5
k=2
def divisibleSumPairs(n, k, arr):
    count=0
    '''
    for i in range(len(arr)):
        m=arr[i]%k
        
        for j in range(len(arr)):
            if arr[j]==m and j!=i :
                count=count+1
    return count
    '''
    for i in range(n):
      for j in range(i+1,n):
          if(arr[i]+arr[j])%k==0:
              count=count+1
    return count
                    
print(divisibleSumPairs(n,k,arr))
            
        