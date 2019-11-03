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

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    j=0
    for i in range (len(ar)):
        if ar[i]>ar[i+1]:
            big=ar[i]
        if big in ar:
            j+=1
    return j
            
        
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))
    

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


