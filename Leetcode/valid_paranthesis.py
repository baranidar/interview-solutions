 #https://leetcode.com/problems/valid-parentheses/  
    def isValid(self, s: str) -> bool:
        from collections import deque
        stack = deque()
        s_list = list(s)
        if len(s) <= 1 or s_list[0] == ")" or s_list[0] == "]" or s_list[0] == "}" or len(s) % 2 != 0:
            return False
        for i in s_list:
            if i in ("{","(","["):
                stack.append(i)
            else:
                if stack:
                    item = stack[-1]
                    match i:
                        case "}":
                            i = "{"
                        case "]":
                            i = "["
                        case ")":
                            i = "(" 
                    if item == i and stack:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
