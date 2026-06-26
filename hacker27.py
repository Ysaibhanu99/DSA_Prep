#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # 1. Count 'a's in a single copy of string s
    count_in_single = s.count('a')
    
    # 2. Find how many full times s repeats in n characters
    full_repeats = n // len(s)
    total_a = full_repeats * count_in_single
    
    # 3. Handle the remaining partial string
    remainder_length = n % len(s)
    # Slice the string to only look at the leftover characters
    total_a += s[:remainder_length].count('a')
    
    return total_a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
