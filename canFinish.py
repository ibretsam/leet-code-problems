"""
207. Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first 
if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. 
So it is impossible.

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
import collections
def canFinish(numCourses, prerequisites):
    pre_map = collections.defaultdict(list)
    for course, preq in prerequisites:
        pre_map[course].append(preq)

    visit = set()
    
    def dfs(course):
        if course in visit:
            return False
        
        if pre_map[course] == []:
            return True
        
        visit.add(course)
        for preq in pre_map[course]:
            if not dfs(preq):
                return False
        visit.remove(course)
        pre_map[course] = []
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False
    return True

# Test cases
print(canFinish(4, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]])) # True
print(canFinish(2, [[1,0]])) # True
print(canFinish(2, [[1,0],[0,1]])) # False
print(canFinish(3, [[1,0],[2,1]])) # True