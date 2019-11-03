#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 16:19:59 2019

@author: abhijithneilabraham
"""
arr=[10,20,20,10,10,30,50,10,20]
def sockMerchant(n, ar):
    ar=list(sorted(ar))
    print(ar)
    i=0
    count=0
    while(i<n-1):
        i+=1
        if ar[i]==ar[i-1]:
            count+=1
            i+=1
    print(count)
    return count
sockMerchant(9,arr)