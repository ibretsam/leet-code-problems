"""
889. Construct Binary Tree from Preorder and Postorder Traversal
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of 
a binary tree of distinct values and postorder is the postorder traversal of the same tree, 
reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

Example 1:
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Example 2:
Input: preorder = [1], postorder = [1]
Output: [1]

Constraints:
    1 <= preorder.length <= 30
    1 <= preorder[i] <= preorder.length
    All the values of preorder are unique.
    postorder.length == preorder.length
    1 <= postorder[i] <= postorder.length
    All the values of postorder are unique.
    It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal 
    of the same binary tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        res = []
        def preorder(node):
            if not node:
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(self)
        return str(res)
    
def constructFromPrePost(preorder, postorder):
    pre_index = [0]
    post_index = [0]
    def construct_tree(preorder, postorder):
        root = TreeNode(preorder[pre_index[0]])
        pre_index[0] += 1

        if root.val != postorder[post_index[0]]:
            root.left = construct_tree(preorder, postorder)
        if root.val != postorder[post_index[0]]:
            root.right = construct_tree(preorder, postorder)
        
        post_index[0] += 1
        return root

    return construct_tree(preorder, postorder)

def constructFromPrePost(preorder, postorder):
    if not preorder:
        return None
    n = len(preorder)
    root = TreeNode(preorder[0])
    if n == 1:
        return root
    l = postorder.index(preorder[1])
    root.left = constructFromPrePost(preorder[1 : l + 2], postorder[: l + 1])
    root.right = constructFromPrePost(preorder[l + 2 :], postorder[l + 1 : n - 2])
    return root

# Example 1
preorder = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]
print(constructFromPrePost(preorder, postorder)) # [1,2,3,4,5,6,7]