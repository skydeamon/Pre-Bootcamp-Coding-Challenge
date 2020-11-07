
"""
Created on 11/04/2020

@author: SkyCharmingDeamon

_Umuzi_
Pre-bootcamp challenges tast 8
"""

def convert_number_to_time(number):
    hr = int(number//60)
    mins = int(number%60)
    hour = 'hour' if(hr==1) else 'hours'
    minute = 'minute' if(mins == 1) else 'minutes'
    return f"{int(number//60)} {hour}, {int(number%60)} {minute}"
