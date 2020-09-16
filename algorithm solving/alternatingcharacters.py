#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:14:10 2020

@author: abhijithneilabraham
"""

def alternatingCharacters(s):
    rs=s[0]
    for i in s:
        if rs[-1]!=i:
            rs+=i
    return len(s)-len(rs)