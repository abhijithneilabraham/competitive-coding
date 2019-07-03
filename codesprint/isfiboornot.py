#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:22:28 2019

@author: abhijithneilabraham
"""
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
            
    return flag
print(solve(10))

             