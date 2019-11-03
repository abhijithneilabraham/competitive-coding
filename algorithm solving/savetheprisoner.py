#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 01:31:00 2019

@author: abhijithneilabraham
"""
a=94431605  
b=679262176
c=5284458
def saveThePrisoner(n, m, s):
	l = (s - 1 + m) % n
	if l == 0:
		l = n
	print(l)
    
saveThePrisoner(a,b,c)