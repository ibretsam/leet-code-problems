"""
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

          4                    4
        /   \                /   \
       2     7      =>      7     2
      / \   / \            / \   / \
     1   3 6   9          9   6 3   1

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

            2                    2
          /   \       =>       /   \
         1     3              3     1

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: [] 

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        if not self:
            return ""
        
        from collections import deque
        q = deque([(self, 0)])
        levels = []
        
        while q:
            node, level = q.popleft()
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val if node else None)
            if node:
                q.append((node.left, level + 1))
                q.append((node.right, level + 1))
        
        # Format the tree structure
        result = ""
        max_level = len(levels)
        max_width = 2 ** (max_level - 1)
        
        for i, level in enumerate(levels):
            space_between = " " * (max_width // (2 ** i))
            line = space_between.join(str(val) if val is not None else " " for val in level)
            result += " " * (max_width // (2 ** (i + 1))) + line + "\n"
        
        return result
from collections import deque
def invertTree(root):
    if not root:
        return root

    # 1. Iterative DFS
    stack = [root]
    while stack:
        curr = stack.pop()

        curr.left, curr.right = curr.right, curr.left

        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)    
    return root

    # 2. Iterative BFS
    # q = deque([root])

    # while q:
    #     curr = q.popleft()

    #     curr.left, curr.right = curr.right, curr.left

    #     if curr.left:
    #         q.append(curr.left)
    #     if curr.right:
    #         q.append(curr.right)
    # return root

    # 3. Recursive
    # root.left, root.right = invertTree(root.right), invertTree(root.left)
    # return root

# Test Cases
# root = [4,2,7,1,3,6,9]
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
print(invertTree(root)) # [4,7,2,9,6,3,1]

# root = [2,1,3]
root = TreeNode(2, TreeNode(1), TreeNode(3))
print(invertTree(root)) # [2,3,1]

# root = []
root = None
print(invertTree(root)) # []