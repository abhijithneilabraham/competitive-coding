#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 23:18:43 2020

@author: abhijithneilabraham
"""

def hcf(a,b):
    for i in range(min((a,b)),0,-1):
        if a%i==0 and b%i==0:
            return i
print(hcf(27,18))
            