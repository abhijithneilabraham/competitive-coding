#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:32:55 2019

@author: abhijithneilabraham
"""

def numbercount(num):
    a=[]
    while num>0:
        a.append(num%10)
        num//=10
    return a
#print(numbercount(123))
def genrot(num):
    b=numbercount(num)
    b=b[::-1]
    for i in range(len(b)-1):
        b=b[-1:]+b[:-1]
        print (b)
genrot(12345)

    