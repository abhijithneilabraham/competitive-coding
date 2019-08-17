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

#!/bin/python3

import math
import os
import random
import re
import sys
a=[3,2,1,3]
# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    b=sorted(ar)
    m=max(b)
    c=0
    for i in b:
        if i==m:
            c+=1
    print(c)
    return c

birthdayCakeCandles(a)        
            
        




