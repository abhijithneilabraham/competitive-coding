#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:44:42 2020

@author: abhijithneilabraham
"""
a=[2,4,2,6,1,7,8,9,2,1]
def candies(n, arr):
    candy_lr = [1]*(len(arr))
    candy_rl = [1]*(len(arr))
    candy = []
    
    # traverses from left to right and assigns candy to students
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            candy_lr[i] = candy_lr[i-1]+1
    
    # traverses from right to left and assigns candy to students        
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>arr[i+1]:
            candy_rl[i] = candy_rl[i+1]+1   
    
    #calculates the total candy needed
    for i in range(0,len(arr)):
        candy.append(max(candy_lr[i],candy_rl[i]))
    print(sum(candy))
    return sum(candy)
        
        
            
def candies(n, arr):
    cl=[1]*n
    cr=[1]*n
    s=0
    
    for i in range(1,n):
        if arr[i-1]<arr[i]:
            cl[i]=cl[i-1]+1
    
    for i in range(n-2,-1,-1):
        if arr[i+1]<arr[i]:
            cr[i]=cr[i+1]+1
    #for i in range(n):
    for i in range(n):
        s+=max(cl[i],cr[i])
    print(s)
    return s
    
        
            
        
            
        
        
        
    
print(candies(len(y),y))
    