#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:37:52 2019

@author: abhijithneilabraham
"""

def dayOfProgrammer(year):
    if year%4==0:
        if year%100==0:
            day="13.09."+str(year)
            print(day)
        else:
            day="12.09."+str(year)
            print(day)
            
        
    else:
        day="13.09."+str(year)
    print(day)
    return day
dayOfProgrammer(2100)