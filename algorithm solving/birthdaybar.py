#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 23:28:54 2019

@author: abhijithneilabraham
"""
s=[1, 2, 1, 3, 2]
def birthday(s, d,m):
    count=0
    s=list(set(s))
    for i in range(len(s)):
        j=0
        while(i+j<len(s) and count<=m ):
            if d-s[i]==s[j]:
                count=count+1
    
            j=j+1
    if len(s)==1 and s[0]==d:
        count=1
    
    return count
    '''
        if d-s[i] in s and : 
            count=count+1
            m=i
            
            
        elif len(s)==1 and s[0]==d:
            count=m
            
    return count
    '''
        
    #print(count//2)
print(birthday(s,3,2))