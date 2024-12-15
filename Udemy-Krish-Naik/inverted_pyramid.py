"""
Function to return an inverted pyramid pattern of '*' of side n as a list of strings.

Parameters:
n (int): The number of rows in the inverted pyramid.

Returns:
list: A list of strings where each string represents a row of the inverted pyramid.
"""
output = []
base = (2*n) - 1
for i in range(base, -1, -2):
    space = (base - i) // 2
    output.append(' ' * space + '*'  * i + ' ' * space)
for i in output:
    print(i)
return output