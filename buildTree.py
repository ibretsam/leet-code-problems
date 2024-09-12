"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree 
and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:

        3
       / \
      9  20
        /  \
       15   7

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]

Constraints:
1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}, {self.left}, {self.right}"

def buildTree(inorder, postorder):
    inorderIdx = {val: idx for idx, val in enumerate(inorder)}

    def helper(l, r):
        if l > r:
            return None
        root = TreeNode(postorder.pop())
        i = inorderIdx[root.val]
        root.right = helper(i + 1, r)
        root.left = helper(l, i - 1)

        return root

    return helper(0, len(inorder) - 1)
# Test cases
print(buildTree([9,3,15,20,7], [9,15,7,20,3])) # [3,9,20,null,null,15,7]
print(buildTree([-1], [-1])) # [-1]
print(buildTree([1, 2], [2, 1])) # [1, null, 2]