#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 02:08:06 2019

@author: abhijithneilabraham
"""
def isprime(b):
    c=True
    for i in range(2,b):
        if b%i==0:
            c=False
    return c
def pri(a):
    count=0
    for i in range(2,a):
        if a%i==0:
            if isprime(i)==True:
                count+=1
    print(count)
    return count
pri(42)
                
            