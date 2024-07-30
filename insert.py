"""
57. Insert Interval
You are given an array of non-overlapping intervals intervals where intervals[i] = [start[i], end[i]] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by start[i]. 
You are also given an interval newInterval = [start, end] that represents the start and end of another 
interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by start[i] and 
intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= start[i] <= end[i] <= 10^5
intervals is sorted by start[i] in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
"""

def insert(intervals, newInterval):
    if intervals == []:
        intervals.append(newInterval)
        return intervals
    res = []
    merged = False
    for interval in intervals:
        if interval[0] >= newInterval[0] and interval[1] <= newInterval[1]:            
            newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]                
            if res and newInterval[0] <= res[-1][1]:
                res.pop()
            res.append(newInterval)
            merged = True
        elif interval[1] >= newInterval[0] and interval[1] <= newInterval[1]: 
            newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            res.append(newInterval)  
            merged = True
        elif interval[0] <= newInterval[1] and interval[1] >= newInterval[1]:
            newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            if res and newInterval[0] <= res[-1][1]:                
                res.pop()
            res.append(newInterval)
            merged = True
        else:
            res.append(interval)
    
    if not merged:
        res.append(newInterval)
    res = sorted(res, key=lambda x: x[0])
    return res

print(insert([[1,3], [6,9]], [2,5])) # [[1,5],[6,9]]
print(insert([[1,2], [3,5], [6,7], [8,10], [12,16]], [4,8])) # [[1,2],[3,10],[12,16]]
print(insert([[1,5]], [2,3]))
print(insert([[1,5]], [0,0]))
print(insert([[0,2],[3,9]], [6,8])) # [[0,2],[3,9]]
print(insert([[0,5],[9,12]], [7,16])) # [[0,5],[7,16]]