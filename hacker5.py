#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    i = len(arr)
    
    # Loop through items directly
    for item in arr:
        if item > 0:
            pos += 1
        elif item < 0:
            neg += 1
        else:
            zero += 1
            
    # Print each ratio formatted to 6 decimal places as HackerRank requires
    print(f"{pos/i:.6f}")
    print(f"{neg/i:.6f}")
    print(f"{zero/i:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
