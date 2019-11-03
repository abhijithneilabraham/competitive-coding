#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 04:16:15 2019

@author: abhijithneilabraham
"""

def camelcase(s):
    c=[ord(i) for i in s]
    count=1
    for j in c:
        if j>=65 and j<=90:
            count+=1
    print(count)
    return count
camelcase("goodDayToday")