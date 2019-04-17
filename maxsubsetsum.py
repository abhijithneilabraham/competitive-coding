#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:58:44 2019

@author: abhijithneilabraham
"""
arr=[2,1,5,8,4]
def maxSubsetSum(arr):
    a=max(arr)
    
    b=arr.index(a)
    '''
    if b%2==0:
        j=0
        c=0
        while j!='\0':
            c+=arr[j]
            j+=2
    else:
        k=1
        d=0
        while k!='\0':
            d+=arr[k]
            k+=2
    print(c,d)
    '''
    print(b)
maxSubsetSum(arr)
            
            
