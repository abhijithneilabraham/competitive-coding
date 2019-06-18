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
    for i in range(len(alice)):
        j=0 
        while len(scores) >j and alice[i]>=scores[j]:
                j+=1
                rank.append(len(scores)+1-j)
        
    print(rank)
climbingLeaderboard(scores,alice)

            