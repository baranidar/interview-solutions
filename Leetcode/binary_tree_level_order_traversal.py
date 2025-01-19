#https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        output = []
        queue = deque()
        queue.append(root)
        output.append([root.val])
        while queue:
            counter = len(queue)
            inner_list = []
            while counter > 0:
                node = queue.popleft()
                # print(f"queue = {queue}\n node = {node}\n output = {output}\n node.left = {node.left}\n node.right = {node.right}", end ="\n\n")
                if node.left:
                    queue.append(node.left)
                    inner_list.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    inner_list.append(node.right.val)
                counter -= 1
                # print(counter, inner_list)
            if inner_list != []:
                output.append(inner_list)
            # print(output)
        return output