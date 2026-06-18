#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    period=s[-2:]
    time_str=s[:-2]
    hh, mm, ss = time_str.split(':')
    if period == "PM" and hh!="12":
        hh= str(int(hh)+12)
    elif period =="AM" and hh=="12":
        hh="00"
    return f"{hh}:{mm}:{ss}"
    
    
    
    # 3. Apply the 12-hour to 24-hour rules
    if period == "PM" and hh != "12":
        hh = str(int(hh) + 12)
    elif period == "AM" and hh == "12":
        hh = "00"
        
    # 4. Return the formatted 24-hour time string
    return f"{hh}:{mm}:{ss}"
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
