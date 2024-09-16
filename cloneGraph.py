"""
133. Clone Graph
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
 
Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, 
the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of 
neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference 
to the cloned graph.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not 
have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Constraints:
The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def __str__(self) -> str:
        """
        Display as a 2D list of all neighbors
        """
        return str([[neighbor.val for neighbor in self.neighbors]])

def cloneGraph(node):
    if not node:
        return None
    old_to_new = {}

    def dfs(node):
        if node in old_to_new:
            return old_to_new[node]
        
        copy = Node(node.val)
        old_to_new[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))
        
        return copy

    return dfs(node)

# Helper function to print the graph
from collections import deque
def print_graph(node):
    if not node:
        print([])
        return
    
    visited = set()
    queue = deque([node])
    result = []

    while queue:
        current = queue.popleft()
        if current.val not in visited:
            visited.add(current.val)
            neighbors = [neighbor.val for neighbor in current.neighbors]
            result.append(neighbors)
            for neighbor in current.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)
    
    print(result)


# Test cases
# [[2,4],[1,3],[2,4],[1,3]]
node = Node(1)
node.neighbors = [Node(2), Node(4)]
node.neighbors[0].neighbors = [node, Node(3)]
node.neighbors[1].neighbors = [node, Node(3)]
print_graph(cloneGraph(node)) # [[2,4],[1,3],[2,4],[1,3]]

# [[]]
node = Node(1)
print_graph(cloneGraph(node)) # [[]]

# []
node = None
print_graph(cloneGraph(node)) # []