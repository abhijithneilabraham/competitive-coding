#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 23:44:33 2020

@author: abhijithneilabraham
"""

def maximumToys(prices, k):
    pr=sorted(prices)
    c=0
    d=0
    for i in pr:
        c+=i
        if c<=k:
            d+=1
        else:
            break
    return d