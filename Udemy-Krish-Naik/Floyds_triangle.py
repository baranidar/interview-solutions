def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    output = []
    list_item_count = 0
    counter = 1
    
    if n == 1:
        output.append('1')
        print(output)
        return output
    
    while list_item_count < n:
        item_string = ""
        space_factor = 0
     
        while space_factor <= list_item_count:
            item_string = item_string + str(counter) + ' '
            space_factor +=  1
            counter += 1
        output.append(item_string.rstrip())
        list_item_count += 1
    
    for i in output:
        print(i)
    return output
        
