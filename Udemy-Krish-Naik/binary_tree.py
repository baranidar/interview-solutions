class BinaryTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def print_tree(root):
    if root is None:
        return
    print(root.data,end=": ")
    if root.left is not None:
        print(f"L -> {root.left.data}", end=", ")
    else:
        print("L -> None", end=" ")
    if root.right is not None:
        print(f"R -> {root.right.data}")
    else:
        print("R -> None")
    print_tree(root.left)
    print_tree(root.right)

def height(node):
    if node is None:
        return 0
    height_left = height(node.left)
    height_right = height(node.right)
    
    return 1 + max(height_left, height_right)

def diameter_tree(node): # can optimize to get height and diameter in one call
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)

    left_diameter = diameter_tree(node.left)
    right_diameter = diameter_tree(node.right)

    return max(left_height+right_height, left_diameter, right_diameter)

def pre_order_traversal(node):
    if node is None:
        return 0
    
    print(node.data, end=" ")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)


def post_order_traversal(node):
    if node is None:
        return 0
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data, end=" ")

def in_order_traversal(node):
    if node is None:
        return 0
    in_order_traversal(node.left)
    print(node.data, end=" ")
    in_order_traversal(node.right)

root = BinaryTreeNode(1)
r_c1 = BinaryTreeNode(2)
r_c2 = BinaryTreeNode(3)
root.left = r_c1
root.right = r_c2
c1_c1 = BinaryTreeNode(4)
c1_c2 = BinaryTreeNode(5)
c2_c1 = BinaryTreeNode(6)
c2_c2 = BinaryTreeNode(7)
r_c1.left = c1_c1
r_c1.right = c1_c2
r_c2.left = c2_c1
r_c2.right = c2_c2
print_tree(root)
print("Diameter of the tree: ", diameter_tree(root))
print("Pre-order-traversal........")
pre_order_traversal(root)
print("Post-order-traversal........")
post_order_traversal(root)
print("In-order-traversal........")
in_order_traversal(root)
'''
   1
 2    3

4  5  6  7
'''