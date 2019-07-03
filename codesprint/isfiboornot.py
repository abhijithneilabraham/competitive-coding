#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:22:28 2019

@author: abhijithneilabraham
"""
'''
8
2
2
3
2
2
34
13
34
'''
def solve(i):
    def fib(n):
        m=1
     
        if n<=1:
           
            return m
        else:
             m=fib(n-1)+fib(n-2)
           
             return m
    flag='IsNotFibo'
    for j in range(i):
        if i==fib(j):
            flag='IsFibo'
            break
            
    return flag
print(solve(34))

             