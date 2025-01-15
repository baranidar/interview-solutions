#https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # rearrange each row in ascending order
    for index, row in enumerate(grid):
        lst = list(row)
        lst.sort()
        row = "".join(lst)
        grid[index] = row
    print(grid)
    ret_value = "YES"
    for i in range(len(grid[0])-1):
        for j in range(len(grid)-1):
            #print(grid[j][i], ord(grid[j][i]),grid[j+1][i], ord(grid[j+1][i]))
            if  ord(grid[j][i]) > ord(grid[j+1][i]):
                ret_value = "NO"
    return ret_value

if __name__ == '__main__':

    fptr = open('/Users/aditibaranidar/Downloads/test_cases.rtf', 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

