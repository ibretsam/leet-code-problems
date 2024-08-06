"""
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
def merge(intervals):    
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    for interval in intervals[1:]:        
        last_interval = res[-1]
        if last_interval[1] >= interval[0]:
            last_interval[1] = max(last_interval[1], interval[1])
        else:
            res.append(interval)
    return res

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[1,4],[0,4]]))
print(merge([[1,4],[2,3]]))
        