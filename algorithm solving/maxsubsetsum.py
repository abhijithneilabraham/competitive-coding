#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:58:44 2019

@author: abhijithneilabraham
"""
arr=[2,1,5,8,4]
def maxSubsetSum(arr):
    c=0
    d=0
    for j in range(0,len(arr),2):
                c+=arr[j]        
    for k in range(1,len(arr),2):
            d+=arr[k]
        
    print(c,d)
maxSubsetSum(arr)
'''
incomplete program
'''
            
            
