"""
572. Subtree of Another Tree
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same 
structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.

Example 1:
        3       4
       / \     / \
      4   5   1   2
     / \
    1   2
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
        3       4
       / \     / \
      4   5   1   2
     / \
    1   2
       /
      0
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-10^4 <= root.val <= 10^4
-10^4 <= subRoot.val <= 10^4
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str([self.val, self.left.val if self.left else None, self.right.val if self.right else None])

"""
Iterative DFS
Time: O(m * n) where m is nodes in root tree and n is nodes in subRoot tree
    - For each node in root tree (m), we might need to check entire subRoot tree (n)
Space: O(h) where h is height of root tree
    - Stack space for DFS traversal
    - Worst case O(m) for skewed tree
"""
def isSubtree(root, subRoot) -> bool:
    def is_identical(s, t):
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        return s.val == t.val and is_identical(s.left, t.left) and is_identical(s.right, t.right)
    stack = [[root, subRoot]]
    while stack:
        node, sub_node = stack.pop()
        if is_identical(node, sub_node):
            return True                    
        else:
            if node.left:
                stack.append([node.left, sub_node])
            if node.right:
                stack.append([node.right, sub_node])        
    return False

"""
String Serialization
Time: O(m + n) for serialization + O(m) for string search = O(m + n)
    - Serializing both trees: O(m + n)
    - String search using KMP algorithm: O(m)
Space: O(m + n)
    - Storing serialized strings for both trees
"""
def isSubtree(root, subRoot) -> bool:
    def serialize(node):
        if not node:
            return '#'
        return f',{node.val}{serialize(node.left)}{serialize(node.right)}'
    
    return serialize(subRoot) in serialize(root)

"""
Merkle Hashing
Time: O(m * h) where h is height of subRoot tree
    - Computing hash for each node: O(m)
    - Each hash comparison involves traversing subRoot: O(h)
Space: O(h)
    - Recursion stack space for DFS
    - Hash storage is constant per node
"""
def isSubtree(root, subRoot) -> bool:
    def hash_node(node):
        if not node:
            return '#'
        left_hash = hash_node(node.left)
        right_hash = hash_node(node.right)
        return hash(f'{node.val},{left_hash},{right_hash}')
    
    def dfs(node):
        if not node:
            return False
        if hash_node(node) == sub_hash:
            return is_identical(node, subRoot)
        return dfs(node.left) or dfs(node.right)
    
    def is_identical(s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return (s.val == t.val and 
                is_identical(s.left, t.left) and 
                is_identical(s.right, t.right))
    
    sub_hash = hash_node(subRoot)
    return dfs(root)

# Test cases
# [3,4,5,1,2]
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
# [4,1,2]
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)
print(isSubtree(root, subRoot)) # Expected: True

# [3,4,5,1,2,null,null,null,null,0]
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(0)
# [4,1,2]
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)
print(isSubtree(root, subRoot)) # Expected: False
