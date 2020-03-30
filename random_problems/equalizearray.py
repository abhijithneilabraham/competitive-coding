#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 01:33:29 2020

@author: abhijithneilabraham
"""

a=[1,2, 3 ,2,2,2,1, 2, 3, 3, 3]
def equalizeArray(arr):
    x=max(arr.count(i) for i in arr)
    print(x)
    return len(arr)-x
    
equalizeArray(a)
