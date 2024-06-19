class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
def leafSequence(root):
    def dfs(node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        return dfs(node.left) + dfs(node.right)
    return dfs(root)
            
def leafSimilar(root1, root2):
    return leafSequence(root1) == leafSequence(root2)
    
    
# print(leafSimilar(TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8))), TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))))
print(leafSimilar(TreeNode(1, TreeNode(2)), TreeNode(2, TreeNode(2)))) 