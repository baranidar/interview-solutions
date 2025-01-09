#https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    rows = len(arr)
    cols = len(arr[0])
    diag_1 = diag_2 = 0
    for i in range(rows):
        diag_1 += arr[i][i]
    

    j = 0
    k = cols - 1
    while j <=   cols - 1 and k > -1:
        print(j,k)
        diag_2 += arr[j][k]
        j += 1
        k -= 1
    print(diag_1, diag_2)
    return abs(diag_1 - diag_2)
'''
00 01 02
10 11 12
20 21 22

00 01 02 03
10 11 12 13
20 21 22 23
30 31 32 33
'''
if __name__ == '__main__':

    arr = [[1,2,3],[4,5,6],[9,8,9]]

    result = diagonalDifference(arr)
    print(result)
