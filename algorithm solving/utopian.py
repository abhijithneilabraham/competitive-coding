#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:35:10 2019

@author: abhijithneilabraham
"""

def utopianTree(n):
    i=1
    j=0
    while(j<n):
       if j%2==0:
           i=i*2
       else:
           i=i+1
       j+=1
    print(i)
    return i

utopianTree(4)
   
    