from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def rightSideView(root):
    if not root:
        return
    q = deque()
    q.append(root)
    res = []
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if i == size - 1:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
    return res

print(rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))))
print(rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))))
print(rightSideView(TreeNode(1, None, TreeNode(3))))