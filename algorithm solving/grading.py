#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 22:46:39 2019

@author: abhijithneilabraham
"""
#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    result=[]
    for i in range(len(grades)):
        if grades[i]<=100 and grades[i]>=0:
            if grades[i]<38:
                result.append(grades[i])
            elif grades[i]%5>=3:
                result.append((int(grades[i]/5)+1)*5)
            else:
                result.append(int(grades[i]))
    
    return result
    #
    # Write your code here.
    #

if __name__ == '__main__':
   

    n = int(input('enter number of students'))

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    res = gradingStudents(grades)
    print(res)

