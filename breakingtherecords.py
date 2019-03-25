#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:02:18 2019

@author: abhijithneilabraham
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    a=[]
    b=[]
    c=[]
    
    for i in range(len(scores)):
        a.append(scores[i])
        if scores[i]>=max(a)and scores[i] not in b:
            b.append(scores[i])
        if scores[i]<=min(a) and scores[i] not in c:
            c.append(scores[i])
    return len(b)-1,len(c-1)

        
scores=[8,20,20,4,2,6,7]        
        


result = breakingRecords(scores)
