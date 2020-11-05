"""
Created on 11/04/2020

@author: SkyCharmingDeamon

_Umuzi_
Pre-bootcamp challenges tast 8
"""

def convert_number_to_time(number):
	return "{} hours, {} minutes".format(int(number//60),int(number%60))
