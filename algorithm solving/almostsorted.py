#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 01:53:28 2020

@author: abhijithneilabraham
"""
arr=[1,5,4,3,2,6]
#arr=[3,1,2]
def almostSorted(arr):
    arr2=sorted(arr)
    a=[arr[i]-arr2[i] for i in range(len(arr))]
    c=0

    mi,ma=a.index(min(a))+1,a.index(max(a))+1
    i=0
    while i<len(a):
        if -a[i] in a and a[i]>0:
            c+=1
      
        i+=1
    if c==0:
        print("no")
    elif c==1:
        print("yes")
        print("swap {} {}".format(ma,mi))
    else:
        print("yes")
        print("reverse {} {}".format(ma,mi))
            
                
    
almostSorted(arr)


    