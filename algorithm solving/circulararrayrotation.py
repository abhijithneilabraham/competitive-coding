#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:47:06 2019

@author: abhijithneilabraham
"""

def circularArrayRotation(a, k, queries):
    new_arr = a[-k%len(a):] + a[:-k%len(a)]
    result = []
    for i in queries:
        result.append(new_arr[i])
    return result