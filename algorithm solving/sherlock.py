#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 22:11:59 2020

@author: abhijithneilabraham
"""

def isValid(s):
    vals={i:s.count(i) for i in s}
    c=list(vals.values())
    counts={i:c.count(i) for i in c}
    print(counts)
    if len(counts)==1:
        return "YES"
    if len(counts)==2:
        keys=list(counts.keys())
        values=list(counts.values())
        if abs(keys[0]-keys[1])==1 or 1 in keys:
            if min(values)==1:
                return "YES"
    return "NO"