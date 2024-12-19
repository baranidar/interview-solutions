def countNegatives(grid):
   counter = 0
   for row in range(len(grid)):
       for column in range(len(grid[0])):
           if grid[row][column] < 0:
               counter += 1
     
   return counter  
