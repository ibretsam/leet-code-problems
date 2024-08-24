"""
637. Average of Levels in Binary Tree
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

        3
       / \
      9   20
    /  \
   15   7

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:

        3
       / \
      9   20
    /  \
   15   7

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
 

Constraints:
The number of nodes in the tree is in the range [1, 104].
-2^31 <= Node.val <= 2^31 - 1
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
def averageOfLevels(root):
    if not root:
        return 0
    q = deque([root])
    avgs = [root.val]
    while q:
        total_node = 0
        curr_sum = 0

        for _ in range(len(q)):
            node = q.popleft()
            
            if node.left:
                q.append(node.left)
                curr_sum += node.left.val
                total_node += 1
            if node.right:
                q.append(node.right)
                curr_sum += node.right.val
                total_node += 1
        if total_node != 0:
            average = curr_sum / total_node
            avgs.append(average)
    
    return avgs
        
# Test case
# [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(averageOfLevels(root)) # [3.0, 14.5, 11.0]

# [3,9,20,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(15)
root.left.right = TreeNode(7)
print(averageOfLevels(root)) # [3.0, 14.5, 11.0]

# [3,1,5,0,2,4,6]
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)
print(averageOfLevels(root)) # [3.0, 3.0, 3.0]