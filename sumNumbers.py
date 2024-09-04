"""
129. Sum Root to Leaf Numbers
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
A leaf node is a node with no children.

Example 1:

        1
       / \
      2   3

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

        4
       / \
      9   0
     / \
    5   1

Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 

Constraints:
The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root):
    if not root: return 0
    curr_num = ''
    sum_list = []
    stack = [(root, curr_num)]

    while stack:
        node, num = stack.pop()
        num += str(node.val)

        if not node.left and not node.right:
            sum_list.append(int(num))
            
        if node.left:
            stack.append((node.left, num))
        if node.right:
            stack.append((node.right, num))
    return sum(sum_list)

# Test cases
# [1,2,3]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(sumNumbers(root)) # 25

# [4,9,0,5,1]
root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
print(sumNumbers(root)) # 1026