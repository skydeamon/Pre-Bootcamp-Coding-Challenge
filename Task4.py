"""
Created on 11/04/2020

@author: SkyCharmingDeamon

_Umuzi_
Pre-bootcamp challenges tast 4: functions/conditionals
A function that takes 2 numbers as input. If either of the numbers is 3 AND the sum of the numbers contains a 3 then return true. Otherwise return false.
"""


def function(a,b):
	return 'True' if( (a or b == 3) and ('3' in list(str(a+b))) ) else 'False'