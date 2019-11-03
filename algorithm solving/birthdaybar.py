#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 23:28:54 2019

@author: abhijithneilabraham
"""
s=[1, 2, 1, 3, 2]
def birthday(s, d,m):
    count=0
    for i in range(len(s)):
        n=s[i:i+m]
        if len(n)==m:
            if sum(n)==d:
                count+=1
                
    print(count)
    return count
            
            
                
        


        
birthday(s,3,2)