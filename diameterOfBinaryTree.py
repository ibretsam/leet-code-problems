"""
543. Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
 
Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-100 <= Node.val <= 100
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root) -> int:
    res = 0
    def dfs(node):
        if not node: return 0
        left = dfs(node.left)
        right = dfs(node.right)
        nonlocal res
        res = max(res, left + right)
        return 1 + max(left, right)
    dfs(root)
    return res

# Test cases
# [1,2,3,4,5]
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(diameterOfBinaryTree(root)) # Expected: 3

# [1,2]
#       1
#      /
#     2
root = TreeNode(1)
root.left = TreeNode(2)
print(diameterOfBinaryTree(root)) # Expected: 1

# [3,1,null,null,2]
#       3
#      / 
#     1  
#      \
#       2
root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
print(diameterOfBinaryTree(root)) # Expected: 2

# [3,2,4,null,null,1]
#       3
#      / \
#     2   4
#        /
#       1
root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.right.left = TreeNode(1)
print(diameterOfBinaryTree(root)) # Expected: 3