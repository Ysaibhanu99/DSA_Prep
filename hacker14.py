#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    
  
    # 1. Turns from the front
    turns_from_front = p // 2
    
    # 2. Turns from the back
    turns_from_back = (n // 2) - (p // 2)
    
    # 3. Return the minimum of the two
    return min(turns_from_front, turns_from_back)

# Examples:
print(pageCount(6, 2))  # Output: 1
print(pageCount(5, 4))  # Output: 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
