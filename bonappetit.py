#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:33:05 2019

@author: abhijithneilabraham
"""
arr=[3, 10, 2, 9]



def bonAppetit(bill, k, b):
    del bill[k]
    s=0
    for i in bill:
        s+=i
    s=s//2
    if b>s:
        print(b-s)
        return b-s
    else:
        print('Bon Appetit')
print(bonAppetit(arr,1,12))