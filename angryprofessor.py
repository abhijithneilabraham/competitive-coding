#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 01:56:02 2019

@author: abhijithneilabraham
"""
arr=[-1,-1,0,1]
def angryprofessor(a,k):
    count=0
    for i in range(len(a)):
        if a[i]<=0:
            count+=1
    if count>=k:
        print("NO")
        return "NO"
    else:
        print("YES")
        return "YES"
angryprofessor(arr,4)