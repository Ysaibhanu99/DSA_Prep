#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Initialize records with the score of the first game
    max_score = scores[0]
    min_score = scores[0]
    
    # Initialize counts for breaking records
    max_breaks = 0
    min_breaks = 0
    
    # Iterate through the remaining games
    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_breaks += 1
        elif score < min_score:
            min_score = score
            min_breaks += 1
            
    # Return the result as [highest, lowest]
    return [max_breaks, min_breaks]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)) + '\n')

    fptr.close()
