#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:04:28 2019

@author: abhijithneilabraham
"""

#N is a fibonacci number if and only 5N^2 + 4 or 5N^2 – 4 is a perfect square 
import math
def solve(number):
    if math.sqrt(5 * number ** 2 + 4).is_integer() or math.sqrt(5 * number ** 2 - 4).is_integer():
        print("IsFibo")
    else:
        print("IsNotFibo")