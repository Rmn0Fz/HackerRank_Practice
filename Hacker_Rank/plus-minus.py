#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    arln = len(arr)
    pos = 0
    neg = 0
    eq = 0
    for i in arr:
        if i > 0:
            pos +=1
        elif i < 0:
            neg += 1
        else:
            eq += 1
    print(pos/arln)
    print(neg/arln)
    print(eq/arln)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
