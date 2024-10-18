"""
427. Construct Quad Tree
Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.
Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. 
Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the 
value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide 
the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.
Quad-Tree format:

You don't need to read this section for solving the problem. This is only if you want to understand 
the output format here. The output represents the serialized format of a Quad-Tree using level order 
traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is 
represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value 
of isLeaf or val is False we represent it as 0.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.

Example 2:
Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:

Constraints:
n == grid.length == grid[i].length
n == 2^x where 0 <= x <= 6
"""

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
    
    def __str__(self):
        return f'Node({self.val}, {self.isLeaf}, {self.topLeft}, {self.topRight}, {self.bottomLeft}, {self.bottomRight})'
    
def construct(grid):
    top_val = grid[0][0]
    isLeaf = True
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != top_val:
                isLeaf = False
                break
    if isLeaf:
        return Node(top_val, 1, None, None, None, None)
    else:
        m = len(grid)
        root = Node(1, 0, None, None, None, None)
        top_left_val = grid[0][0]
        isTopLeftLeaf, isTopRightLeaf, isBottomLeftLeaf, isBottomRightLeaf = True, True, True, True

        for row in range(m // 2):            
            for col in range(m // 2):
                if grid[row][col] != top_left_val:
                    isTopLeftLeaf = False
                    break
        if isTopLeftLeaf:
            root.topLeft = Node(top_left_val, 1, None, None, None, None)
        else:
            root.topLeft = construct([row[:m // 2] for row in grid[:m // 2]])
        
        top_right_val = grid[0][m // 2]
        for row in range(m // 2):
            for col in range(m // 2, m):
                if grid[row][col] != top_right_val:
                    isTopRightLeaf = False
                    break
        if isTopRightLeaf:
            root.topRight = Node(top_right_val, 1, None, None, None, None)
        else:
            root.topRight = construct([row[m // 2:] for row in grid[:m // 2]])
        
        bottom_left_val = grid[m // 2][0]
        for row in range(m // 2, m):
            for col in range(m // 2):
                if grid[row][col] != bottom_left_val:
                    isBottomLeftLeaf = False
                    break
        if isBottomLeftLeaf:
            root.bottomLeft = Node(bottom_left_val, 1, None, None, None, None)
        else:
            root.bottomLeft = construct([row[:m // 2] for row in grid[m // 2:]])
                    
        bottom_right_val = grid[m // 2][m // 2]
        for row in range(m // 2, m):
            for col in range(m // 2, m):
                if grid[row][col] != bottom_right_val:
                    isBottomRightLeaf = False
                    break
        if isBottomRightLeaf:
            root.bottomRight = Node(bottom_right_val, 1, None, None, None, None)
        else:
            root.bottomRight = construct([row[m // 2:] for row in grid[m // 2:]])
        
        return root
    
def construct(grid):
    def is_leaf(grid, x, y, size):
        val = grid[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if grid[i][j] != val:
                    return False, val
        return True, val
    
    def construct_rec(grid, x, y, size):
        isLeaf, val = is_leaf(grid, x, y, size)
        if isLeaf:
            return Node(val, True, None, None, None, None)
        
        half = size // 2
        topLeft = construct_rec(grid, x, y, half)
        topRight = construct_rec(grid, x, y + half, half)
        bottomLeft = construct_rec(grid, x + half, y, half)
        bottomRight = construct_rec(grid, x + half, y + half, half)

        return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
    
    return construct_rec(grid, 0, 0, len(grid))

# Test cases
grid1 = [[0,1],[1,0]]
root1 = construct(grid1)
print(root1)

grid2 = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
root2 = construct(grid2)
print(root2)

grid3 = [[1,1],[1,1]]
root3 = construct(grid3)
print(root3)