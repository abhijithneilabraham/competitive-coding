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
    
    for i in scores:
        a.append(i)
        if i>max(a):
            b.append(i)
        if i<min(a):
            c.append(i)
    print(len(b),len(c))

        
scores=[3,4,2,6,7]        
        


result = breakingRecords(scores)
