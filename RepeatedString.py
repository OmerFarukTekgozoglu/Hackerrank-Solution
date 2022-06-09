#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


from collections import Counter
def repeatedString(s, n):
    # Write your code here
    lengthOfString = len(s)
    if lengthOfString < 2 and s == "a":
        return n
 
    elif s != "a" and lengthOfString <2:
        return 0
    
    repeatTimes = n // lengthOfString
    additionalString = n % len(s)
    additionS = s[:int(additionalString)].count("a")
    alphaDict = Counter(s)
    print (alphaDict["a"])
    if alphaDict["a"] != 0:
        repeatedAalpha = repeatTimes * alphaDict["a"] + additionS
    else:
        return 0
    
    return math.floor(repeatedAalpha)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
