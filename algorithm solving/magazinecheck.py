#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 01:54:12 2020

@author: abhijithneilabraham
"""

def checkMagazine(magazine, note):
    d={}
    for i in magazine:
        d.setdefault(i,1)
    for i in note:
        if i in d:
            d[i]-=1
        else:
            print("No")
            return
    for i in d:
        if d[i]<0:
            print("No")
            return
    print("Yes")
    return
            
            
checkMagazine(["two","times","three","is","not","four"],["two","times","two","is","four"])