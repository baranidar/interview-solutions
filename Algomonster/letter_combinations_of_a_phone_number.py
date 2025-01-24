def letterCombinations(digits):
#this one uses DFS and backtracking to achieve solution
    letters = []
    res = []
    n = len(digits)
    digits_to_alpha = {"2":"abc", "3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    digits = list(digits)
    for digit in digits:
        letters.append(digits_to_alpha[digit])
    letters = ''.join(letters)
    
    def dfs(level, path):
        if level == n and path.reverse() not in res:
            res.append("".join(path))
            return
        for letter in letters:
            if letter in path:
                continue
            path.append(letter)
            #print(letter, path)
            dfs(level + 1, path)
            path.pop()

    dfs(0, [])
    for index, item in enumerate(res):
        item = list(item)
        item.sort()
        item = "".join(item)
        res[index] = item
    return list(set(res))

res = letterCombinations("234")
print(res)