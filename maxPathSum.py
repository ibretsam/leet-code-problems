"""
124. Binary Tree Maximum Path Sum
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence 
has an edge connecting them. A node can only appear in the sequence at most once. Note that the path 
does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:

          1
         / \
        2   3

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:

         -10
         / \
        9  20
          /  \
         15   7

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 
Constraints:
The number of nodes in the tree is in the range [1, 3 * 10^4].
-1000 <= Node.val <= 1000
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"{self.val}, {self.left}, {self.right}"

def maxPathSum(root):
    res = float("-inf")

    def dfs(node):
        nonlocal res
        if not node:
            return 0
        left_max = dfs(node.left)
        right_max = dfs(node.right)
        left_max = max(left_max, 0)
        right_max = max(right_max, 0)

        res = max(res, node.val + left_max + right_max)
        return node.val + max(left_max, right_max)

    dfs(root)
    return res


# Test cases
# [1,2,3,null,null,4,5]
node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.right.left = TreeNode(4)
node.right.right = TreeNode(5)
print(maxPathSum(node)) # 12

# [1,2,3]
node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
print(maxPathSum(node)) # 6

# [-10,9,20,null,null,15,7]
node = TreeNode(-10)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)
print(maxPathSum(node)) # 42