"""
114. Flatten Binary Tree to Linked List
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to 
the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:

     1
    / \
   2   5       => 1 -> 2 -> 3 -> 4 -> 5 -> 6
  / \   \
 3   4   6

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
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
        
    
def flatten(root):
    """
    Do not return anything, modify root in-place instead.
    """
    while root:
        # if root.left is not None
        if root.left:
            # set curr node as root.left
            curr = root.left
            # traverse to the extreme right of curr
            while curr.right:
                curr = curr.right
            # join curr.right to root.right
            curr.right = root.right
            # put root.left to root.right
            root.right = root.left
            # make root.left as None
            root.left = None
        # now go to the right of the root
        root = root.right

# Test Cases
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
print(flatten(root)) # [1, None, 2, None, 3, None, 4, None, 5, None, 6]

root = TreeNode(0)
print(flatten(root)) # [0, None]

root = TreeNode(1)
print(flatten(root)) # [1, None]
