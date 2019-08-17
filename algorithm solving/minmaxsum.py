#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 00:34:37 2019

@author: abhijithneilabraham
"""
a=[1,2,3,4,5]
def miniMaxSum(arr):
    b=sorted(arr)
    s=0
    mini=0
    for i in range(len(b)):
        if i!=0:
            s+=b[i]
        if i!=len(b)-1:
            mini+=b[i]
    print(s,mini)
miniMaxSum(a)