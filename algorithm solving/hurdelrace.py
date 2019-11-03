#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 02:52:59 2019

@author: abhijithneilabraham
"""
ht=[1,6,3,5,2]
def hurdleRace(k, height):
    m=max(height)
    if k>=m:
        print(0)
        return 0
    else:
        print(m-k)
        return m-k
hurdleRace(4,htc)
        