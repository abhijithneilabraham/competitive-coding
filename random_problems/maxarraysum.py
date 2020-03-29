#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 19:04:58 2019

@author: abhijithneilabraham
"""
a=[3,7,1,1,6,1]
def f(arr): 
    one = 0
    two = 0
     
    for i in arr: 
          
        # Current max excluding i (No ternary in  
        # Python) 
        new = two if two>one else one 
        print(new,'new')
         
        # Current max including i 
        one = two + i 
        print(one,'one')
        two = new 
        print(two,'two')
      
    # return max of incl and excl 
    return (two if two>one else one) 
  
        
        
print(f(a))
    
        
    
        
        
        
    


#I guess this one went wrong
        
        
        
        