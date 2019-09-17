#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 02:26:11 2019

@author: abhijithneilabraham
"""

def timeConversion(s):
    t=s.split(":")
    if "PM" in t[2]:
        if t[0]!='12':
            t[0]=str(int(t[0])+12)
    else:
        if t[0]=="12":
            t[0]="00"
    
    n=":".join(t)
    print(n[:-2])
    return n[:-2]
        
                
            
timeConversion("12:45:54PM")


    
        