#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:41:44 2020

@author: abhijithneilabraham
"""

def acmTeam(topic):
    x=[]
    c=0
    cr=[]
    for i in range(len(topic)):
        for j in range(1,len(topic)):
            c=0
            m=topic[i]+topic[j]
            for k in str(m):
                if int(i)>0:
                    c+=1
            cr.append(c)
    x=[max(c),c.count(max(c))]
    return x

    
                
            
