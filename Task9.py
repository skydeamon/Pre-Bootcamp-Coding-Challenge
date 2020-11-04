"""
Created on 11/04/2020

@author: SkyCharmingDeamon

_Umuzi_
Pre-bootcamp challenges tast 9
"""

# Sums multiples of 3 and 5
def sum_multiples(number):
	multiples = []
	for i in range(number+1):
		if(i%3==0 or i%5==0):
			multiples.append(i)
	print(multiples)
	return sum(multiples)