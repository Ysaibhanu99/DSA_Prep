#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

from collections import Counter

def pickingNumbers(a):
    counts = Counter(a)
    max_length = 0
    
    # Check each unique number 'x' present in the input
    for x in counts:
        # Check combination of (x, x+1)
        max_length = max(max_length, counts[x] + counts[x + 1])
        
    return max_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
