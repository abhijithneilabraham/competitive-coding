#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:05:25 2019

@author: abhijithneilabraham
"""
arr=[1,4,4,4,5,3]
def migratoryBirds(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print(freq[4])
                
               
           
       
       
migratoryBirds(arr)
            
