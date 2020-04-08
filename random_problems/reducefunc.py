#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:04:51 2020

@author: abhijithneilabraham
"""
from fractions import Fraction
from functools import reduce
def product(fracs):
    o=1
    e=1
    for i in range(len(fracs)):
        e=e*fracs[i].numerator
        o=o*fracs[i].denominator
    m=[]
    m.append(e)
    m.append(o)
 
    t = reduce(Fraction,m)# complete this line with a reduce statement
    return t.numerator, t.denominator
