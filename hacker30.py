#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Sort the array to easily find the smallest elements
    arr.sort()
    result = []
    n = len(arr)
    
    i = 0
    while i < n:
        # The number of sticks remaining is the total minus current index
        result.append(n - i)
        
        # Move past all sticks of the current shortest length
        current_shortest = arr[i]
        while i < n and arr[i] == current_shortest:
            i += 1
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
