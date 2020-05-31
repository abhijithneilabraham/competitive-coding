#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 06:33:59 2020

@author: abhijithneilabraham
"""

def countSwaps(a):
    c=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[j]<a[i]:
                c+=1
                a[i],a[j]=a[j],a[i]
    print('Array is sorted in '+str(c)+ ' swaps.')
    print('First Element: '+str(a[0]))
    print('Last Element: '+str(a[-1]))

arr=[3,2,1]
countSwaps(arr)