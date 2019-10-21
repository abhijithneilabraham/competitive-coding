#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:23:20 2019

@author: abhijithneilabraham
"""
import datetime
start=datetime.datetime.now()
def stepPerms(n): 
    a=stepPerms
    if n==0 or n==1:
        return 1
    elif n==2:
        return n
    else:
        return a(n-3)+a(n-2)+a(n-1)
stop=datetime.datetime.now()
print(stepPerms(10))
print(stop-start)