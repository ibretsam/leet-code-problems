"""
112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that 
adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22

          5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1

Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5

            1
           / \
          2   3
          
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
 

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):
    if not root:
        return False
    stack = [(root, root.val)]

    while stack:
        node, curr_sum = stack.pop()
        if node:
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    return True
        
            if node.left:
                stack.append((node.left, curr_sum + node.left.val))
            if node.right:
                stack.append((node.right, curr_sum + node.right.val))
    return False

# Test cases
# [5,4,8,11,null,13,4,7,2,null,null,null,1]
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)
print(hasPathSum(root, 22)) # True

# [1,2,3]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(hasPathSum(root, 5)) # False

# []
root = None
print(hasPathSum(root, 0)) # False

# [1,2]
root = TreeNode(1)
root.left = TreeNode(2)
print(hasPathSum(root, 2)) # False