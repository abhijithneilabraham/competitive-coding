#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 02:21:51 2019

@author: abhijithneilabraham
"""

'''
solving a hackerrank problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.

arr =[6,1,2,7,4] #list(map(int, input().rstrip().split()))
j=[]
k=[]
for i in range(len(arr)-1):
    if arr[i+1]>arr[i]:
        j.append(arr[i+1])
        k.append(arr[i])
    else:
        j.append(arr[i])
        k.append(arr[i+1])
        
print(j,k)

