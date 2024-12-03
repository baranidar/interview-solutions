from collections import deque

def reverse_string_list(input):
    stack = deque()
    my_list = list(input)
    reverse_list = []
    for i in my_list:
        stack.append(i)
    count = len(stack)
    for j in range(len(stack)):
        reverse_list.append(stack.pop())
    print (''.join(reverse_list))
        

def reverse_string_stack(input):
    stack = deque()
    reverse_list = ""
    for i in input:
        stack.append(i)
    while len(stack) > 0:
        reverse_list += stack.pop()
    print(reverse_list)
        
        

reverse_string_list("Hello World")
reverse_string_stack("Hello World")
