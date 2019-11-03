#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 23:08:19 2019

@author: abhijithneilabraham
"""

ht=[1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
def designerPdfViewer(h, word):
    
    w=[h[ord(i)-97] for i in word]
    print(w)
    c=max(w)*len(word)
    
        
    print(c)
    return c
        
        
    
    
designerPdfViewer(ht,'abc')
    