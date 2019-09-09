#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 01:05:26 2019

@author: abhijithneilabraham
"""

def beautifulDays(i, j, k):
    count=0
    for n in range(i,j+1):
        m=str(n)[::-1]
        if abs(n-int(m))%k==0:
            count+=1
    print(count)
    return count
beautifulDays(20,23,6)