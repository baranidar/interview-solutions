# https://leetcode.com/problems/minimum-falling-path-sum/
def minFallingPathSum(matrix) -> int:
    rows = -len(matrix)-1
    columns = len(matrix[0])

    for row in range(-1,rows,-1):
        #print(row, end="\n")
        if row != -1:
            for column in range(len(matrix[0])):
                #print(row, column)
                if column == 0:
                    #print("first", matrix[row][column], min(matrix[row + 1][column], matrix[row + 1] [column + 1]))
                    matrix[row][column] = matrix[row][column] + min(matrix[row + 1][column], matrix[row + 1] [column + 1])
                elif column == columns - 1:
                    #print("last", matrix[row][column], min(matrix[row + 1] [column - 1], matrix[row + 1][column]))
                    matrix[row][column] = matrix[row][column] + min(matrix[row + 1] [column - 1], matrix[row + 1][column])
                else:
                    #print("middle", matrix[row][column], min(matrix[row + 1] [column - 1], matrix[row + 1][column], matrix[row + 1] [column + 1]))
                    matrix[row][column] = matrix[row][column] + min(matrix[row + 1] [column - 1], matrix[row + 1][column], matrix[row + 1] [column + 1])

            # for x in matrix:
            #     print(x)
    print(min(matrix[0]))

minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])