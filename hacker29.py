#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

from collections import Counter

def equalizeArray(arr):
    # Count frequencies of all elements
    counts = Counter(arr)
    
    # Find the maximum frequency of any single element
    max_freq = max(counts.values())
    
    # Deletions = Total elements minus the most frequent element count
    return len(arr) - max_freq

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
