"""
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
 
Example 1:

    2
   / \
  1   3

Input: root = [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        """
        Return a tree like this:
            1
           / \
          2   5       
         / \   \
        3   4   6

        """
        if self.left is None and self.right is None:
            return str(self.val)
        return f"{self.val} \n{self.left} {self.right}"

def isValidBST(root):
    def in_order_traversal(node):
        nonlocal prev
        if not node:
            return True
        left = in_order_traversal(node.left)
        if prev and prev.val >= node.val:
            return False
        prev = node
        right = in_order_traversal(node.right)
        return left and right
    prev = None
    return in_order_traversal(root)

# Test Cases
# [2, 1, 3]
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(isValidBST(root)) # Expected output: True

# [5, 1, 4, null, null, 3, 6]
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(isValidBST(root)) # Expected output: False

# [2, 2, 2]
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)
print(isValidBST(root)) # Expected output: False

# [5,4,6,null,null,3,7]
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)
print(isValidBST(root)) # Expected output: False