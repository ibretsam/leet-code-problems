"""
239. Sliding Window Maximum
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array 
to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
 
Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]
 
Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""
import heapq
from collections import deque
def maxSlidingWindow(nums, k: int):
    """
    Using Deque
    Time Complexity: O(n)
    Space Complexity: O(n)    
    """
    l, r = 0, 0
    res = []
    q = deque()
    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            res.append(nums[q[0]])
            l += 1
        r += 1
    return res

def maxSlidingWindow(nums, k):
    """
    Using Max Heap
    Time Complexity: O(n)
    Space Complexity: O(n)    
    """
    heap = []
    res = []
    for i in range(len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        if i >= k - 1:
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            res.append(-heap[0][0])
    return res

# Example 1:
nums = [1,-1]
k = 1
print(maxSlidingWindow(nums, k)) #Output: [3,3,5,5,6,7]

# Example 2:
nums = [1]
k = 1
print(maxSlidingWindow(nums, k)) #Output: [1]