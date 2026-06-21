#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
from collections import Counter

def migratoryBirds(arr):
    bird_counts = Counter(arr)
    
    # Track the highest frequency and the best bird ID
    max_count = 0
    best_bird = float('inf')
    
    # Iterate through the tallies to find the winner
    for bird, count in bird_counts.items():
        # Condition 1: Current bird has a higher count
        # Condition 2: Current bird has same count but a smaller ID
        if count > max_count:
            max_count = count
            best_bird = bird
        elif count == max_count and bird < best_bird:
            best_bird = bird
            
    return best_bird
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
