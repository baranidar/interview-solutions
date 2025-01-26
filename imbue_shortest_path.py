import random


def expected_length(field, k):
    if k == 0:
         return 0
    output = -1

    # Get the rows and columns to determine size of matrix(field)
    rows = len(field)
    cols = len(field[0])

    # Get K random numbers to pick in the matrix
    chosen_spots = []
    while len(chosen_spots) < k:
            r = random.randint(0,rows-1)
            c = random.randint(0,cols-1)
            to_add = [r,c]
            if to_add not in chosen_spots:
                 chosen_spots.append(to_add)

    def dfs(field, rows, cols, chosen_spots, path):
        i = chosen_spots[0][0]
        j = chosen_spots[0][1]
        path.append([i,j])
        length = 0
        while i < rows and j < cols and chosen_spots not in path:
            # Can we navigate this path?
            if i+1 < rows and field[i+1][j] != '#':
                path.append([i+1,j])
                length += 1
                i += 1
                continue
            if i+1 < rows and j+1 < cols and field[i+1][j+1] != "#": 
                path.append([i+1,j+1])
                length += 1
                i += 1
                j += 1
                continue
            if j+1 < cols and field[i][j+1] != "#": 
                path.append([i,j+1])
                length += 1
                j += 1
                continue
            if i-1 > 0 and field[i-1][j] != "#": 
                path.append([i-1,j])
                i -= 1
                length += 1
                continue
            if j-1 > 0 and field[i][j-1] != "#": 
                path.append([i,j-1])
                j -= 1
                length += 1
                continue
            if i-1 > 0 and j-1 > 0 and field[i-1][j-1] != "#": 
                path.append([i-1,j-1])
                i -= 1
                j -= 1
                length += 1
                continue
            if len(chosen_spots) == len(set(path)):
                return length 

    output = dfs(field, rows, cols, chosen_spots, path = [])    
    return output


if __name__ == "__main__":
    field = ["*#..#", ".#*#.", "*...*"]
    k = 2
    result = expected_length(field,k)
    print(result)

'''
*#..#
.#*#.
*...*
'''