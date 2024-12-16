def rotate(self, matrix: List[List[int]]) -> None:
    #transpose matrix
    for row in range(len(matrix)):
        for col in range(row+1, len(matrix[0])):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp
        
    #reverse each row
    for row in matrix:
        row.reverse()
