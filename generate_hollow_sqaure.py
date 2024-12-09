def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    output = []
    if n == 1:
        output.append('*')
        return output
    output.append('*' * n)
    filler ='*' + ' ' * (n-2) + '*'
    for i in range(n-2):
        output.append(filler)
    output.append('*' * n)
    return output
