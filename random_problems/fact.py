#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 23:56:53 2019

@author: abhijithneilabraham
"""

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
print(factorial(6))
        