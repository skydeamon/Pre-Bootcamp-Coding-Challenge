"""
Created on 11/04/2020

@author: SkyCharmingDeamon

_Umuzi_
Pre-bootcamp challenges tast 6:
A function that takes in three numbers and returns the maximum number.
"""

import math

def maximum(a,b,c):
    maxim = 0
    if(a>b and b>c):
        maxim = a
    elif(b>c and c>a):
        maxim= b
    else:
        maxim = c
    return maxim
