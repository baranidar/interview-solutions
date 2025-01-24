#https://leetcode.com/problems/valid-palindrome/
def isPalindrome(s: str) -> bool:
    import re
    regex = re.compile('[^A-Za-z0-9]')
    s = regex.sub('',s).lower()
    print(s)
    return s[0::] == s[::-1]

print(isPalindrome('A man, a plan, a canal: Panama'))