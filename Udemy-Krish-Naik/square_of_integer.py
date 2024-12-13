# Problem Description: You are given an integer n. Your task is to return a square pattern of size n x n made up of the character '*', represented as a list of strings.

output_list = [''] * n
new_list  = list(map(lambda i:'*' * n, output_list))

return new_list

# -------------------------------------------------------

output_list = []
for i in range(n):
    output_list.append('*' * n)

return output_list
