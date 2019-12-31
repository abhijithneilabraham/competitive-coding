#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 01:54:12 2020

@author: abhijithneilabraham
"""

def checkMagazine(magazine, note):
    d={}
    for i in magazine:
        d[i]=0
    for i in note:
        d[i]-=1
    for i in magazine:
        d[i]+=1
    for i in d:
        if d[i]<1 or i not in magazine:
            print("No")
            return
    print("Yes")
    return
            
            
checkMagazine(["two","times","three","is","not","four"],["two","times","two","is","four"])