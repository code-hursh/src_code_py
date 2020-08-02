
import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    s = 0
    for i in ar:
        s += i
    return s

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
