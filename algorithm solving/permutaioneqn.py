#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:58:28 2019

@author: abhijithneilabraham
"""
p=[5,2,1,3,4]

def permutationEquation(p):
    c=[]
    for i,val in enumerate(p):
        if i+1 in p:
            c.append(p.index(p.index(i+1)+1)+1)
    print(c)
        
permutationEquation(p)
        