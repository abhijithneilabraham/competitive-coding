#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:46:30 2019

@author: abhijithneilabraham
"""

def pageCount(n, p):
    count=0
   
    if n==p or abs(n-p)==1 :
        return count
    else:
        count=abs(n-p)//2
        return count-1
            
          
               
               
  
    
    print(count-1)
    return count-1
        
n=int(input())
p=int(input())
print(pageCount(n,p))