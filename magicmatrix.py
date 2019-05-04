#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 22:27:23 2019

@author: abhijithneilabraham
"""
a=[[4,9,2],[3,5,7],[8,1,5]]

def magicsquare(a):
    k=0
    l=0
    for i in range(3):
        for j in range(3):
            k+=j
            #if(l!=k):
            print(min(a[i][:]))
        l=k
        #print(k)
#print(magicsquare(a))