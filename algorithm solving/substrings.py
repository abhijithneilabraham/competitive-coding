#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 20:25:33 2020

@author: abhijithneilabraham
"""

def twoStrings(s1, s2):
    for i in s2:
        if i in s1:
            print("YES")
            return "YES
    print("NO")
    return "NO"
