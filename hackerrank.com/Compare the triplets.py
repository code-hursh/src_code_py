## !/bin/python3

import math
import os
import random
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    aP = bP = 0
    for i in range(3):
        if a[i] > b[i]:
            aP += 1
        elif a[i] < b[i]:
            bP += 1
    return(aP,bP)

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print('[%d,%d]'%(result[0],result[1]))

