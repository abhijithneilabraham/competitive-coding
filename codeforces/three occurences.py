#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:17:52 2020

@author: abhijithneilabraham
"""
a='1 2 3 4 3 4 2 1 3 4 2 1'

b=list(map(int,a.split()))
n=len(b)//3

c=0 
for i in range(0,len(b),3):
    for j in range(n+1):
        if i+j*3<=n*3:
            arr=b[i:i+(j*3)]
            if len(arr)%3==0 and arr:
                counts=[arr.count(i)%3 for i in set(arr)]    
                if not any(counts):
                    print(i,i+j*3,arr,i)
                    c+=1
print(c)



