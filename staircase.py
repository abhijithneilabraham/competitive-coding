#!/bin/python3

import math
import os
import random
import re
import sys
n = int(input())
# Complete the staircase function below.
def staircase(n):


    

   
    for s in range(1, n + 1):
        
        print(' ' * (n - s) + '#' * s)


    
staircase(n)
