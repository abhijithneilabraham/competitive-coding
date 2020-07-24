#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 14:56:30 2020

@author: abhijithneilabraham
"""

def checkMagazine(magazine, note):
    if len(set(magazine)&set(note))==len(note):
        print("Yes")
    else:
        print("No")
