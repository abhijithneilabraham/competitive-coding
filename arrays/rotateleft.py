#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:35:02 2019

@author: abhijithneilabraham
"""
a=[1,2,3,4]
def rotLeft(b, d):
    a=b
    c=[]
    a=b[d:]
    c=b[0:d]
    a=a+c
    print(a)
rotLeft(a,2)
        