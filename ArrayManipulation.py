#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
def arrayManipulationSolutionFromOthers(n, queries):
    # Write your code here
    xs = [0]*(n+2)
    for q in queries:
        a,b,k = q
        xs[a] += k
        xs[b+1] -= k
    
    answer = 0
    current = 0
    
    for x in xs:
        current += x
        answer = max(answer, current)
    
    return answer
    
def arrayManipulation_solutionOne(n, queries):
    # Write your code here
    initialDict = {item:0 for item in range(1,n+1)}
    for que in queries:
        low,high = que[:-1][0],que[:-1][1]
        val = que[-1]
        tempDict = {_:val for _ in range(low,high+1)}
        for k,v in tempDict.items():
            initialDict[k] += tempDict[k]
    idxOfMax = max(initialDict,key=initialDict.get)
    return initialDict[idxOfMax]

def arrayManipulation_solutionTwo(n, queries):
    # Write your code here
    initialArray = [0]*n
    for que in queries:
        firstIndex = que[0]-1
        secondIndex = que[1]
        val = que[-1]
        newValues = [val for _ in range(firstIndex,secondIndex)]
        
        initialArray[firstIndex:secondIndex] = [temp+_ for temp,_ in zip(initialArray[firstIndex:secondIndex],newValues)]
    return max(initialArray)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulationSolutionFromOthers(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
