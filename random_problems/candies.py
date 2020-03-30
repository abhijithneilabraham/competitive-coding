#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:44:42 2020

@author: abhijithneilabraham
"""
a=[2,4,2,6,1,7,8,9,2,1]
def candies(n, arr):
    cl=[1]*n
    cr=[1]*n
    s=0
    
    for i in range(1,n):
        if arr[i-1]<arr[i]:
            cl[i]=cl[i-1]+1
    
    for i in range(n-2,-1,-1):
        if arr[i+1]<arr[i]:
            cr[i]=cl[i+1]+1
    #for i in range(n):
    for i in range(n):
        s+=max(cl[i],cr[i])
    print(s)
    return s
        
        
            
            
    
        
            
        
            
        
        
        
    
print(candies(len(a),a))
    