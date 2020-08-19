#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 02:40:39 2020

@author: abhijithneilabraham
"""
def strParam(strParam):
    u=lambda x:'_' if x==' 'or not x.isalnum() else x
    strParam=[u(i).lower() for i in strParam]
    return ''.join(strParam)

print(strParam("cats and Dogs*are#awesome"))