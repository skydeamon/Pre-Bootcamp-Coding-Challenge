"""
Created on 11/04/2020

@author: SkyCharmingDeamon

_Umuzi_
Pre-bootcamp challenges tast 5:
A function that takes in three numbers. These numbers represent the lengths of the sides of a triangle. The function should return the area of a triangle.
"""

import math

def function(a,b,c):
	theta = math.acos((a**2 + b**2 - c**2)/a*b)
	area = (1/2) *a*b*math.sin(theta)
	return area