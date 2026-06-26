#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    shared = 5       # Day 1 starts with 5 people
    cumulative = 0   # Total likes start at 0
    
    for day in range(n):
        liked = shared // 2        # Floor division gets half the viewers
        cumulative += liked        # Add today's likes to the total
        shared = liked * 3         # Next day's viewers (those who liked * 3)
        
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
