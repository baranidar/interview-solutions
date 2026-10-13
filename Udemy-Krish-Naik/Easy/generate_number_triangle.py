
def generate_number_triangle(n):
    triangle_list = []
    for i in range(1, n+1):
        triangle_list.append(' '.join(str(i) for x in range(1, i+1)))
    return ' \n'.join(triangle_list)

print(generate_number_triangle(5))