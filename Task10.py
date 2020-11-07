"""
Created on 11/04/2020

@author: SkyCharmingDeamon

_Umuzi_
Pre-bootcamp challenges tast 10
"""

# Print the vowels in a string
def vowels(string):
    vows = ['a','e','i','o','u']
    present = ''
    for letter in list(string):
        if(letter.lower() in vows):
            present += letter
    print(present)
