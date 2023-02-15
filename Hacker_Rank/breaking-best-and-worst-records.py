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
    # Write your code here
    hi_scr = scores[0]
    count_h = 0
    low_scr = scores[0]
    count_low = 0
    for i in scores:
        if i > hi_scr:
            hi_scr = i
            count_h += 1
        elif i < low_scr:
            low_scr = i
            count_low += 1
        else:
            pass
    return [count_h, count_low]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
