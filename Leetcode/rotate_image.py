#https://leetcode.com/problems/rotate-image/

def rotate(matrix) -> None:
    #transpose matrix
    for row in range(len(matrix)):
        for col in range(row+1, len(matrix[0])):
            print(row,col)
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp
    
    print(matrix)
        
    #reverse each row
    for row in matrix:
        row.reverse()


rotate([[1,2,3],[4,5,6],[7,8,9]])

'''
1 2 3
4 5 6
7 8 9

1 4 7
2 5 8
3 6 9
'''