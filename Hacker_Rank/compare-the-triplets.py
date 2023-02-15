#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    first = 0
    second = 0
    
    if a[0] > b[0]:
        first += 1
    elif a[0] < b[0]:
        second +=1
    else:
        pass
    if a[1] > b[1]:
        first += 1
    elif a[1] < b[1]:
        second +=1
    else:
        pass
    if a[2] > b[2]:
        first += 1
    elif a[2] < b[2]:
        second +=1
    else:
        pass
    
    return first, second
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
