"""
100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:
The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4
"""
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
    
def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# Test Cases
# p = [1,2,3], q = [1,2,3]
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(isSameTree(p, q)) # True

# p = [1,2], q = [1,null,2]
p = TreeNode(1, TreeNode(2))
q = TreeNode(1, None, TreeNode(2))
print(isSameTree(p, q)) # False

# p = [1,2,1], q = [1,1,2]
p = TreeNode(1, TreeNode(2, TreeNode(1)), TreeNode(1, TreeNode(2)))
q = TreeNode(1, TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2)))
print(isSameTree(p, q)) # False

# p = [0,-5], q = [0,-8]
p = TreeNode(0, TreeNode(-5))
q = TreeNode(0, TreeNode(-8))
print(isSameTree(p, q)) # False