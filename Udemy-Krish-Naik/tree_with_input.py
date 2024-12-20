from collections import deque

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.children = []
    
def print_tree(node):
    if node is None:
        return
    print()
    print(node.data,end=":")
    for children in node.children:
        print(children.data, end=",")
    for children in node.children:
        print_tree(children)
        
def get_input_level_wise():
    my_queue = deque()
    data = input("Enter the data for the root node: ")
    root = TreeNode(data)
    my_queue.append(root)
    
    while my_queue:
        node = my_queue.popleft()
        children = int(input(f"Enter the number of children for node {node.data}: "))
        for child in range(children):
            child_data = int(input(f"Enter the data for child {child + 1} of node {node.data}: "))
            child_node = TreeNode(child_data)
            node.children.append(child_node)
            my_queue.append(child_node)
    return root


output = get_input_level_wise()
print_tree(output)
