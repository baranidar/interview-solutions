"""
Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.

Parameters:
n (int): The number of rows in the rectangle.
m (int): The number of columns in the rectangle.

Returns:
list: A list of strings where each string represents a row of the rectangle pattern.
"""
output = []
if n == 1 and m == 1:
    output.append('*' * m)
    return output
output.append('*' * m)
for i in range(n-2):
    output.append('*' * (m))
output.append('*' * m)
return output
