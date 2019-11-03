#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:27:25 2019

@author: abhijithneilabraham
"""
a=[1,2,5,3,7,8,6,4]

def minimumBribes(a):
    b=sorted(a)
    print(b)
    count=0
    c=[]
    i=0
    while(i<len(a)-1):
        if a[i]-b[i] and a[i]-b[i+1]  >2:
            print("Too Chaotic")
        else:
            if (a[i])>b[i]:
                count+=(a[i]-b[i])
                
                
        i+=1
    print(count+1)
            
minimumBribes(a)
    