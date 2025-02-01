#https://leetcode.com/problems/roman-to-integer/
#there is a much efficient way to do this with less lines of code but the underlying logic is the same
def roman_to_integer(s):
    if len(s) == 0:
        return ''
    i = 0
    table = {
        "I": 1, "V":5, "X":10, "L": 50, "C":100, "D":500, "M":1000}
    total = 0
    while i <= len(s)-1:
        if i == len(s) - 1:
            total = total + table[s[i]]
            break
        if s[i] == "I":
            if s[i+1] == "V":
                total = total  + table["V"] - table["I"]
                i += 2
                continue
            elif s[i+1] == "X":
                total = total + table["X"] - table["I"]
                i += 2
                continue
            else:
                total = total + table["I"]
                i += 1
                continue
        if s[i] == "X":
            if s[i+1] == "L":
                total = total  + table["L"] - table["X"]
                i += 2
                continue
            elif s[i+1] == "C":
                total = total + table["C"] - table["X"]
                i += 2
                continue
            else:
                total = total + table["X"]
                i += 1
                continue
        if s[i] == "C":
            if s[i+1] == "D":
                total = total  + table["D"] - table["C"]
                i += 2
                continue
            elif s[i+1] == "M":
                total = total + table["M"] - table["C"]
                i += 2
                continue
            else:
                total = total + table["C"]
                i += 1
                continue
        total = total + table[s[i]]
        i += 1
    return total

result = roman_to_integer('MCMXCIV')
print(result)

'''
Alt from leetcode
class Solution:
    def romanToInt(self, s: str) -> int:
        charMap = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        res = 0
        idx = 0
        while idx < len(s):
            if idx+1 < len(s):
                if charMap[s[idx]] >= charMap[s[idx+1]]:
                    res += charMap[s[idx]]
                    idx += 1
                else:
                    res += charMap[s[idx+1]] - charMap[s[idx]]
                    idx += 2
            else:
                res += charMap[s[idx]]
                idx += 1
        return res
'''