#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:21:54 2020

@author: abhijithneilabraham
"""

def appendAndDelete(s, t, k):
    minstring=min([s,t], key=len)
    maxstring=max([s,t],key=len)
    lma=len(maxstring)
    lmi=len(minstring)
    if s==t and k>=0 or set(s)==set(t) or k>=lma+lmi:
        return "Yes"
    s=''
    for i in range(len(minstring)):
        if minstring[i]==maxstring[i]:
            s+=minstring[i]
        else:
            ls=2*len(s)
            l=lma+lmi-ls
            if l==k or k>lma+lmi:
                return "Yes"
    return "No"