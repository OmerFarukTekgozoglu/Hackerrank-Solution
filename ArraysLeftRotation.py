#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    # Write your code here
    
    if len(a) <=1:
        return a
        
    if d >= len(a):
        reducedRot = d % len(a)
        auxArray = a * (reducedRot-1)
        rotatedArray = auxArray[len(a)+d:(2*len(a))+d]
        
    
    else:
        rotatedArray = a[:]
        reducedRot = len(a) - d
        for k in range(reducedRot):
            temp = rotatedArray.pop()
            rotatedArray.insert(0,temp)
            

    return rotatedArray

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
