#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    output = ''
    for item in k:
        if isAlnum(item):
            offset = ord('A') if item.isupper() else ord('a')
            output += chr(offset + (ord(item) - offset + s) %26)
        elif item.isnumeric():
            output += str((int(item) + s) % 10)
        else:
            output+= item
    return output

def isAlnum(letter):
    if letter.isalpha():
        return True
    else:
        return False

if __name__ == '__main__':
    s = 98 #input()
    k = '159357lcfd' #int(input().strip())
    result = caesarCipher(s, k)
    print(result)