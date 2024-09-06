"""
102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level). 

Example 1:

        3
       / \
      9  20
        /  \
       15   7

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
 

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return root
    
    q = deque([root])
    res = [[root.val]]
    while q:
        curr_level = []
        for _ in range(len(q)):
            node = q.popleft()                
            if node.left:
                curr_level.append(node.left.val)
                q.append(node.left)

            if node.right:
                curr_level.append(node.right.val)
                q.append(node.right)
        if curr_level:
            res.append(curr_level)
    
    return res

# Test cases
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(levelOrder(root))  # Expected output: [[3], [9, 20], [15, 7]]

root = TreeNode(1)
print(levelOrder(root))  # Expected output: [[1]]

root = None
print(levelOrder(root))  # Expected output: []