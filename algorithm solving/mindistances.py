#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 21:34:01 2020

@author: abhijithneilabraham
"""
a=[7 ,1 ,3 ,4 ,1 ,7]
a=[1,2,3,4,10]
def minimumDistances(a):
    mindist=len(a)
    flag=False
    for i,j in enumerate(a):
        dist=a.index(j,i)-a.index(j)
        if dist!=0 and dist<mindist:
            mindist=dist  
            flag=True
    if not flag:
        return -1
    return mindist
    
print(minimumDistances(a))

            
            
            
    