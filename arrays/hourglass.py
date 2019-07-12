#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 13:07:19 2019

@author: abhijithneilabraham
"""
arr=[[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0 ,0 ,2 ,4 ,4 ,0],
[0, 0, 0, 2, 0, 0],
[0 ,0 ,1 ,2 ,4 ,0]]
def hourglassSum(arr):
    s=[]
    for i in range(2,len(arr[0])):
        for j in range(2,len(arr)):
            sum1=arr[j-2][i]+arr[j-2][i-1]+arr[j-2][i-2]+arr[j-1][i-1]+arr[j][i]+arr[j][i-1]+arr[j][i-2]
           
        
            s.append(sum1)
    print(max(s))
hourglassSum(arr)
        
        
      
    
