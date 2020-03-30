#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 02:56:22 2020

@author: abhijithneilabraham
"""

def abbreviation(a, b):
    c=0
    for i in b:
        if i.lower() in a or i.upper() in a:
            c+=1
    for j in a:
        if j.isupper() and j not in b:
            print("NO")
            return "NO"
    if c!=len(b):
        print("NO")
        return "NO"
    else:
        print("YES")
        return "YES"
        
    
            
        
        
    
    

            
abbreviation("VLKHNlpsrlrvfxftslslrrh","VLKHN")
    