#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:05:25 2019

@author: abhijithneilabraham
"""
arr=[6,6,6,4,6,3]
def migratoryBirds(arr):
    a=[0]*len(arr)
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
            a.insert(i,freq[i])
        else:
            freq[i]=1
            a.insert(i,freq[i])
       for key,values in freq.items:
           if key==max(a):
               print(key)
            
        
        
                
               
           
       
       
migratoryBirds(arr)
            
