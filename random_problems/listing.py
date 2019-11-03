#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 00:09:00 2019

@author: abhijithneilabraham
"""

a=[i for i in range(7)]
c=a[-2%len(a):]+a[:-2%len(a)]
    
print(c)
    