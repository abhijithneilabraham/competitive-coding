#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 04:25:22 2020

@author: abhijithneilabraham
"""
a=[5 ,4 ,4 ,2 ,2 ,8]
def cutTheSticks(arr):
    res=[]
    while(len(arr)!=0):
        res.append(len(arr))

        
        m=min(arr)

        
        while 1:
            if m in arr:
                arr.remove(m)
            else:
                break
        arr=[i-m for i in arr]
    
    return res
        
        
print(cutTheSticks(a))