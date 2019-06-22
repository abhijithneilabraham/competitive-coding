#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:05:25 2019

@author: abhijithneilabraham
"""
arr=[6,6,6,4,6,3]
def migratoryBirds(arr):
 
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
            
        else:
            freq[i]=1
           
    print(max(freq))
    for key,values in freq.items():
        
        if values==max(freq):
            
            print(key)
            return key
            
        
        
                
               
           
       
       
migratoryBirds(arr)
            
