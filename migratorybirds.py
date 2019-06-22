#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:05:25 2019

@author: abhijithneilabraham
"""
arr=[1,4,4,4,5,3]
def migratoryBirds(arr):
    a=[0]*len(arr)
    for i in range(len(arr)):
        a[arr[i]] += 1
    print( a.index(max(a)))
        
        
                
               
           
       
       
migratoryBirds(arr)
            
