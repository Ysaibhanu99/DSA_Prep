#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    # Calculate the distance from A to C
    distance_A = abs(x - z)
    
    # Calculate the distance from B to C
    distance_B = abs(y - z)
    
    # Compare distances and return the result
    if distance_A < distance_B:
        return "Cat A"  # Point A reaches first
    elif distance_B < distance_A:
        return "Cat B"  # Point B reaches first
    else:
        return "Mouse C"  # Both reach at the same time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
