"""
530. Minimum Absolute Difference in BST
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any 
two different nodes in the tree.

Example 1:

          4
         / \
        2   6
       / \
      1   3

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

         1
        / \
       0   48
          /  \
         12   49

Input: root = [1,0,48,null,null,12,49]
Output: 1
 
Constraints:
The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 10^5
 
Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"{self.val}, {self.left}, {self.right}"

def getMinimumDifference(root):
    stack = [root]
    res = float("inf")
    while stack:
        node = stack.pop()
        if node.left:
            curr = node.left
            if not curr.right:
                res = min(res, node.val - curr.val)
            while curr and curr.right:
                res = min(res, node.val - curr.right.val)
                curr = curr.right
            stack.append(node.left)
        if node.right:
            curr = node.right
            if not curr.left:
                res = min(res, curr.val - node.val)
            while curr and curr.left:
                res = min(res, curr.left.val - node.val)
                curr = curr.left
            stack.append(node.right)
    return res

# Test Cases
# [4,2,6,1,3]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(getMinimumDifference(root)) # 1

# [1,0,48,null,null,12,49]
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(48)
root.right.left = TreeNode(12)
root.right.right = TreeNode(49)
print(getMinimumDifference(root)) # 1

# [600,424,612,null,499,null,689]
root = TreeNode(600)
root.left = TreeNode(424)
root.right = TreeNode(612)
root.left.right = TreeNode(499)
root.right.right = TreeNode(689)
print(getMinimumDifference(root)) # 12
