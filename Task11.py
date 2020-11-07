"""
Created on 11/04/2020

@author: SkyCharmingDeamon

_Umuzi_
Pre-bootcamp challenges tast 11
"""

# Retruns common letters between two strings
def common(str1,str2):
    comm = []
    for let1 in list(str1):
        for let2 in list(str2):
            if(let2==let1 and (let1 not in common)):
                common.append(let1)
    return ",".join(common)
