#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 02:41:01 2020

@author: abhijithneilabraham
"""

def howManyGames(p, d, m, s):
    c=0
    tot=0
    while s-tot>0:
        tot+=p
        if s-tot<0:
            continue
        elif p>m:
            p=p-d if p-d>m else m
        else:
            p=m 
        c+=1

    return c
#16,2,1,9981
print(howManyGames(95 ,68 ,66, 2249))
