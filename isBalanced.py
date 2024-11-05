"""
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node 
never differs by more than one.

Example 1:
     3
    / \
   9  20
     /  \
    15   7
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
        1
       / \
      2   2
     / \
    3   3
   / \
  4   4
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
 
Constraints:
The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"TreeNode({self.val})"

"""
Perform redundant depth-first search for each node to check if the tree is balanced
Time complexity: O(n^2) (worst case) where n is the number of nodes in the tree
Space complexity: O(n) where n is the number of nodes in the tree
"""
def isBalanced(root) -> bool:
    def dfs(node, height):
        if not node:
            return height
        return max(dfs(node.left, height + 1), dfs(node.right, height + 1))
    def is_balanced(node, height):
        left = dfs(node.left, height)
        right = dfs(node.right, height)
        return abs(left - right) <= 1
    
    if not root:
        return True
    stack = [[root, 0]]
    while stack:
        node, height = stack.pop()
        if not is_balanced(node, height):
            return False
        if node.left:
            stack.append([node.left, height + 1])
        if node.right:
            stack.append([node.right, height + 1])
    return True

"""
Perform single depth-first search to check if the tree is balanced
Time complexity: O(n) where n is the number of nodes in the tree
Space complexity: O(n) where n is the number of nodes in the tree
"""
def isBalanced(root) -> bool:
    def check_balance(node):
        if not node:
            return 0, True
        
        left_height, left_balanced = check_balance(node.left)
        right_height, right_balanced = check_balance(node.right)

        current_height = max(left_height, right_height) + 1
        current_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        
        return current_height, current_balanced
    _, balanced = check_balance(root)
    return balanced

# Test cases
# [1,2,2,3,null,null,3,4,null,null,4]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = None
root.right.left = None
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = None
root.right.right.left = None
root.right.right.right = TreeNode(4)
print(isBalanced(root))  # False