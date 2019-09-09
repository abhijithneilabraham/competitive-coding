#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 01:18:19 2019

@author: abhijithneilabraham
"""

def viralAdvertising(n):
    sh=5
    li=sh//2
    c=2
    for i in range(n-1):
        sh=li*3
        li=sh//2
        c+=li
    print(c)
    return c
viralAdvertising(3)
        
        
        