"""
104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the 
farthest leaf node. 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
 
Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
"""
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        res = []
        stack = [self]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            else:
                res.append(None)
        return str(res)
    
def maxDepth(root):
    if not root:
        return 0
    
    # 1. Iterative DFS
    stack = [[root, 1]]
    res = 1
    while stack:
        node, depth = stack.pop()
        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return res

    # 2. Iterative BFS
    # q = deque()
    # q.append(root)
    # res = 0
    # while q:
    #     for _ in range(len(q)):
    #         node = q.popleft()
    #         if node.left:
    #             q.append(node.left)
    #         if node.right:
    #             q.append(node.right)
    #     res += 1
    # return res

    # 3. Recursive DFS
    # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Test cases
# [3,9,20,null,null,15,7]
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(maxDepth(root)) # 3

# [1,null,2]
root = TreeNode(1, None, TreeNode(2))
print(maxDepth(root)) # 2

