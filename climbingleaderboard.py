#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 02:09:03 2019

@author: abhijithneilabraham
"""
scores=[100, 90, 85, 80, 75, 60]

alice=[0, 65, 77, 90, 102]
def climbingLeaderboard(scores, alice):
    rank=len(scores)
    count=0
    for i in range(len(alice)):
        for j in scores:
            if alice[i]>j:
            
                rank=rank-1
                break
        print(rank)
climbingLeaderboard(scores,alice)

            