#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 02:09:03 2019

@author: abhijithneilabraham
"""
scores=[100, 90, 85, 80, 75, 60]

alice=[0, 65, 77, 90, 102]

def climbingLeaderboard(scores, alice):
    scores=sorted(list(set(scores)))
    rank=[]
    j=0
    for i in alice:
        while len(scores) >j and i>=scores[j]:
                j+=1    
        rank.append(len(scores)+1-j)
        
    print(rank)
    return rank
climbingLeaderboard(scores,alice)

            