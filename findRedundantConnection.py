"""
684. Redundant Connection
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. 
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge 
between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, 
return the answer that occurs last in the input.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 
Constraints:
n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""
def findRedundantConnection(edges):
    """
    Union Find Algorithm
    - Time Complexity: O(E * α(V)) where V is the number of vertices and E is the number of edges and α is the inverse 
    Ackermann function
    - Space Complexity: O(V)
    """
    parent = [i for i in range(len(edges) + 1)]
    size = [1] * (len(edges) + 1)

    def find(n):
        p = parent[n]
        while p != parent[p]:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False
        
        if size[p1] > size[p2]:
            parent[p2] = p1
            size[p1] += size[p2]
        else:
            parent[p1] = p2
            size[p2] += size[p1]
        return True

    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]
        
def findRedundantConnection(edges):
    """
    Depth-First Seach
    - Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
    - Space Complexity: O(V)
    """
    n = len(edges)
    adjacent = [[] for _ in range(n + 1)]
    for u, v in edges:
        adjacent[u].append(v)
        adjacent[v].append(u)

    visited = [False] * (n + 1)
    cycle = set()
    cycle_start = -1

    def dfs(node, parent):
        nonlocal cycle_start
        if visited[node]:
            cycle_start = node
            return True

        visited[node] = True
        for neighbor in adjacent[node]:
            if neighbor == parent:
                continue
            if dfs(neighbor, node):
                if cycle_start != -1:
                    cycle.add(node)
                if node == cycle_start:
                    cycle_start = -1
                return True
        return False
    
    dfs(1, -1)

    for u, v in reversed(edges):
        if u in cycle and v in cycle:
            return [u, v]

# Test cases
print(findRedundantConnection([[1,2],[1,3],[2,3]])) # Expected: [2,3]
print(findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]])) # Expected: [1,4]
print(findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5],[4,5]])) # Expected: [4,5]