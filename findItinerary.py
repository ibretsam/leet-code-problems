"""
332. Reconstruct Itinerary
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. 
Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, 
you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 
Constraints:
1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
"""
from collections import defaultdict, deque
def findItinerary(tickets):
    """
    Using DFS with backtracking
    Time Complexity: O(E!) where E is number of edges (tickets)
    Space Complexity: O(E + V) where V is number of vertices (airports)
    """
    adj = defaultdict(deque)
    tickets.sort()
    for src, dst in tickets:
        adj[src].append(dst)
    res = ["JFK"]
    
    def dfs(airport):
        if len(res) == len(tickets) + 1:
            return True
        if airport not in adj:
            return False
        
        # Store destinations to restore if path fails
        for _ in range(len(adj[airport])):
            dst = adj[airport].popleft()
            res.append(dst)
            if dfs(dst):
                return True
            res.pop()
            adj[airport].append(dst)
        return False
    
    dfs("JFK")
    return res

from collections import defaultdict
import heapq
def findItinerary(tickets):
    """
    Using Hierholzer's Algorithm with min-heap
    Time Complexity: O(E * log(E)) where E is number of edges
    Space Complexity: O(E + V) where V is number of vertices
    """
    adj = defaultdict(list)
    for src, dst in tickets:
        heapq.heappush(adj[src], dst)
    
    route = []
    def dfs(airport):
        while adj[airport]:
            dfs(heapq.heappop(adj[airport]))
        route.append(airport)
    
    dfs("JFK")
    return route[::-1]

# Example 1
# tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# print(findItinerary(tickets)) # Output: ["JFK","MUC","LHR","SFO","SJC"]
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# print(findItinerary(tickets)) # Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
tickets = [["JFK","SFO"],["SFO", "JFK"],["JFK","ATL"]]
print(findItinerary(tickets)) # Output: ['JFK', 'SFO', 'JFK', 'ATL']