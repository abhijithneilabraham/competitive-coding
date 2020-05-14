#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:46:29 2020

@author: abhijithneilabraham
"""
a=[i for i in range(2,8)]
d={}
b=[i for i in range(5,15)]
c={}
e=[i for i in range(4,14)]
f={}
for i in range(10):
    c[i]=1
    d[i]=1
    f[i]=1
print(c,d,f)
# for i in range(10):
#     if b[i] in c.keys():
#         c[b[i]]+=1
#     else:
#         c[b[i]]=1
l=[a,b,e]
m=[c,d,f]
for i,j in zip(l,m):
    for k in i:
        if k in j.keys():
            j[k]+=1
print(c,d,f)
        
import pandas as pd       
n=pd.DataFrame(columns=['aa'])
from statistics import mean
print(mean(a))
