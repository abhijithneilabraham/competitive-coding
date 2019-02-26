#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 23:22:54 2019

@author: abhijithneilabraham
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    c=0
    d=0
    for i in range(len(apples)):
        if a+apples[i]>=s and a+apples[i]<=t:
            c+=1
    for j in range(len(oranges)):
        if b+oranges[j]>=s and b+oranges[j]<=t:
            d+=1
    return c,d
            
            
            
    

if __name__ == '__main__':
    print('enter")
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
    
