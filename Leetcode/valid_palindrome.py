#https://leetcode.com/problems/valid-palindrome/
def isPalindrome(s: str) -> bool:
    import re
    regex = re.compile('[^A-Za-z0-9]')
    s = regex.sub('',s).lower()
    print(s)
    return s[0::] == s[::-1]


def isPalindrome_twopointers(s):
    i = 0
    j = len(s) - 1
    while  i <= j:
        if not (s[i].isalpha() or s[i].isnumeric()):
            i  += 1
            continue
        if not (s[j].isalpha() or s[j].isnumeric()):
            j  -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

#print(isPalindrome('A man, a plan, a canal: Panama'))
print(isPalindrome_twopointers('A man, a plan, a canal: Panama'))