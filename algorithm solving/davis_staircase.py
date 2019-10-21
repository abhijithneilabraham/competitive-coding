#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:23:20 2019

@author: abhijithneilabraham
"""

def stepPerms(n): 
    if n==0 or n==1:
        return 1
    elif n==2:
        return n
    else:
        return stepPerms(n-3)+stepPerms(n-2)+stepPerms(n-1)
print(stepPerms(10))