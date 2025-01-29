#https://leetcode.com/problems/valid-palindrome-ii/description/

def valid_palindrome(s):

    if len(s) == 0:
        return False
    
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            skip_Left = s[left+1:right+1]
            skip_right = s[left:right]
            return (skip_Left == skip_Left[::-1]) or (skip_right == skip_right[::-1])
        left += 1
        right -= 1
    return True

print(valid_palindrome('amanbama'))

'''
Works but does not perform well for larger inputs
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False
        
        if s == s[::-1]:
            return True
        else:
            i = 0
            j = len(s) - 1

            while i < j:
                l = s[:i]+s[i+1:]
                r = s[:j]+s[j+1:]
                if l == l[::-1] or r == r[::-1]:
                    return True
                i += 1
                j -= 1
                
            return False
'''