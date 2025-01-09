#https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

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
    pos = 0
    neg = 0
    zero = 0
    total = len(arr)

    for i in arr:
        if i == 0:
            zero+= 1
        if i < 0:
            neg+= 1
        if i > 0:
            pos+= 1
        print(pos, neg, zero)
    print(f"{pos/total:.6f}\n {neg/total:.6f}\n {zero/total:.6f}\n")


if __name__ == '__main__':
    # n = int(input().strip())
    # arr = list(map(int, input().rstrip().split()))

    plusMinus([1, 1, 0, -1, -1])
