#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 02:38:07 2020

@author: abhijithneilabraham
"""

def maxSubsetSum(a):
    i=0
    j=0
    for k in a:
        x=j if j>i else i
        i=j+k
        j=x
    return(j if j>i else i)
