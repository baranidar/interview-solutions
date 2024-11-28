from collections import deque

def reverse_string(input):
    stack = deque()
    my_list = list(input)
    reverse_list = []
    for i in my_list:
        stack.append(i)
    count = len(stack)
    for j in range(len(stack)):
        reverse_list.append(stack.pop())
    print (''.join(reverse_list))
        
        

reverse_string("Hello World")
