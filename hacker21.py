#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    max_height = 0
    
    # Step 1: Find the maximum height among the letters in the word
    for char in word:
        # ord(char) - ord('a') converts 'a'->0, 'b'->1, ..., 'z'->25
        index = ord(char) - ord('a')
        letter_height = h[index]
        
        if letter_height > max_height:
            max_height = letter_height
            
    # Step 2: Calculate total area (Width * Max Height)
    # Width is simply the total number of letters in the word
    width = len(word)
    return width * max_height    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
