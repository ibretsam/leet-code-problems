"""
1028. Recover a Tree From Preorder Traversal
We run a preorder depth-first search (DFS) on the root of a binary tree.
At each node in this traversal, we output D dashes (where D is the depth of this node), 
then we output the value of this node.  If the depth of a node is D, the depth of its 
immediate child is D + 1.  The depth of the root node is 0.
If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

Example 1:
Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:
Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

Example 3:
Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]

Constraints:
    The number of nodes in the original tree is in the range [1, 1000].
    1 <= Node.val <= 10^9
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        """
        Display the tree in preorder traversal
        """
        res = []
        def preorder(node):
            if not node:
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(self)
        return str(res)

def recoverFromPreorder(traversal: str):
    """
    Time complexity: O(n) where n is length of traversal string
    Space complexity: O(h) where h is height of tree
    """
    stack = []
    i = 0
    while i < len(traversal):
        level = 0
        while i < len(traversal) and traversal[i] == '-':
            level += 1
            i += 1
        num = 0
        while i < len(traversal) and traversal[i].isdigit():
            num = num * 10 + int(traversal[i])
            i += 1
        
        node = TreeNode(num)

        while stack and len(stack) > level:
            stack.pop()
        
        if stack:
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
        stack.append(node)
    return stack[0]

# Example 1
traversal = "1-2--3--4-5--6--7"
print(recoverFromPreorder(traversal)) # 1, 2, 5, 3, 4,