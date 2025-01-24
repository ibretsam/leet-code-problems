"""
802. Find Eventual Safe States
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by 
a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning 
there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path 
starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Example 1:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

Example 2:
Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.

Constraints:
    n == graph.length
    1 <= n <= 10^4
    0 <= graph[i].length <= n
    0 <= graph[i][j] <= n - 1
    graph[i] is sorted in a strictly increasing order.
    The graph may contain self-loops.
    The number of edges in the graph will be in the range [1, 4 * 10^4].
"""

def eventualSafeNodes(graph):
    """
    Time complexity: O(V log V + E) due to sorting
    Space complexity: O(V)
    """
    visited = set()
    path = set()  # Track current path
    terminals = []
    safes = set()
    
    for i in range(len(graph)):
        if not graph[i]:  # Empty list = terminal
            terminals.append(i)
            safes.add(i)
    
    def dfs(node):
        if node in safes:  # Already known safe
            return True
        if node in path:  # Found cycle
            return False
        
        path.add(node)
        all_safe = True
        
        for dest in graph[node]:
            if dest not in visited:
                if not dfs(dest):
                    all_safe = False
                    break
            elif dest not in safes:  # If visited but not safe
                all_safe = False
                break
                
        path.remove(node)  # Backtrack
        if all_safe:
            safes.add(node)
        visited.add(node)
        return all_safe

    for i in range(len(graph)):
        if i not in visited:
            dfs(i)
            
    return sorted(list(safes))

def eventualSafeNodes(graph):
    """
    Time complexity: O(V + E)
    Space complexity: O(V)    
    """
    n = len(graph)
    # 0: not visited, 1: visiting, 2: safe
    state = [0] * n
    
    def dfs(node):
        # If currently visiting - found cycle
        if state[node] == 1:
            return False
        # If already processed
        if state[node] == 2:
            return True
            
        # Mark as visiting
        state[node] = 1
        
        # Check all neighbors
        for nei in graph[node]:
            if not dfs(nei):
                return False
                
        # Mark as safe
        state[node] = 2
        return True

    return [i for i in range(n) if dfs(i)]

print(eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])) # [2,4,5,6]
print(eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]])) # [4]
print(eventualSafeNodes([[],[0,2,3,4],[3],[4],[]])) # [0,1,2,3,4]