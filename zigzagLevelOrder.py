"""
103. Binary Tree Zigzag Level Order Traversal
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:

     3
    / \
   9   20
      /  \
     15   7

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"{self.val}, {self.left}, {self.right}"

from collections import deque
def zigzagLevelOrder(root):   
    res = []
    def bfs(node, level):
        if not node:
            return
        q = deque()
        q.append(node)
        while q:
            curr_level = []
            for _ in range(len(q)):
                curr_node = q.popleft()
                curr_level.append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)

            if level % 2 == 1:
                curr_level = curr_level[::-1]
            res.append(curr_level)
            level += 1
    bfs(root, 0)
    return res

# Test cases
# [3,9,20,null,null,15,7]
node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)
print(zigzagLevelOrder(node)) # [[3], [20, 9], [15, 7]]

# [1]
node = TreeNode(1)
print(zigzagLevelOrder(node)) # [[1]]

# []
node = None
print(zigzagLevelOrder(node)) # []