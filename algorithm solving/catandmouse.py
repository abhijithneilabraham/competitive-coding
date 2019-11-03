#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:57:40 2019

@author: abhijithneilabraham
"""

def catAndMouse(x, y, z):
        if abs(x-z)>abs(y-z):
            print("Cat B")
            return str("Cat B")
        elif abs(x-z)<abs(y-z):
            print("Cat A")
            return str("Cat A")
        else:
             print("Mouse C")
             return str("Mouse C")