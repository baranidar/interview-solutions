#https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    int_dict = {}
    for i in a:
        if i in int_dict:
            int_dict[i] += 1
        else:
            int_dict[i] = 1
    print(int_dict)
    return (next(key for key, value in int_dict.items() if value == 1))

if __name__ == '__main__':
    a = [1, 2, 3, 1, 2]
    result = lonelyinteger(a)
    print(result)

