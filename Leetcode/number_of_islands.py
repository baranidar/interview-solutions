#https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        matrix = grid

        def dfs(matrix, r, c):
            queue  = deque()
            queue.append((r,c))

            while queue:
                r,c = queue.popleft()

                if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or matrix[r][c] != '1':
                    continue
                matrix[r][c] = '0'
                queue.append((r, c+1))
                queue.append((r, c-1))
                queue.append((r+1, c))
                queue.append((r-1, c))

        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if matrix [row] [col] == '1':
                    islands += 1
                    dfs(matrix, row, col)
        return islands
    
#--------------------------------------another approach

def find_number_of_islands(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    islands = 0
    for row in range(rows):
        for col in range(cols):
            if matrix [row] [col] == '1':
                islands += 1
                dfs(matrix, row, col)
    return islands

def dfs(matrix, r, c):
    print(matrix, r, c)
    if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]) or matrix[r][c]  == '0':
        return
    matrix[r][c] = '0'
    dfs(matrix,r, c+1)
    dfs(matrix,r, c-1)
    dfs(matrix, r+1, c)
    dfs(matrix, r-1, c)


if __name__ == "__main__":
    input = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    output = find_number_of_islands(input)
    print(output)


