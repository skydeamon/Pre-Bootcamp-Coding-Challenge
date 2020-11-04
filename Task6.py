"""
Created on 11/04/2020

@author: SkyCharmingDeamon

_Umuzi_
Pre-bootcamp challenges tast 6:
A function that takes in three numbers and returns the maximum number.
"""

import math

def Maximum(a,b,c):
	maximum = 0
	if(a>b and b>c):
		maximum = a
	elif(b>c and c>a):
		maximum= b
	else:
		maximum = c
	return maximum