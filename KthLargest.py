"""
703. Kth Largest Element in a Stream
You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. 
This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the 
kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the 
sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool 
of test scores so far.

Example 1:
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output: [null, 4, 5, 5, 8, 8]

Explanation:
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3); // return 4
kthLargest.add(5); // return 5
kthLargest.add(10); // return 5
kthLargest.add(9); // return 8
kthLargest.add(4); // return 8

Example 2:
Input:
["KthLargest", "add", "add", "add", "add"]
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]
Output: [null, 7, 7, 7, 8]

Explanation:
KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
kthLargest.add(2); // return 7
kthLargest.add(10); // return 7
kthLargest.add(9); // return 7
kthLargest.add(9); // return 8
 
Constraints:
0 <= nums.length <= 10^4
1 <= k <= nums.length + 1
-10^4 <= nums[i] <= 10^4
-10^4 <= val <= 10^4
At most 10^4 calls will be made to add.
"""
from heapq import heappush, heappop
class KthLargest:

    def __init__(self, k, nums):
        self.heap = []
        self.larger = []
        self.k = k
        for num in nums:
            heappush(self.heap, -num)
        while len(self.larger) < k and self.heap:
            heappush(self.larger, -heappop(self.heap))

    def add(self, val: int) -> int:
        if len(self.larger) < self.k:
            heappush(self.larger, val)
        elif val < self.larger[0]:
            heappush(self.heap, -val)
        else:
            heappush(self.heap, -heappop(self.larger))
            heappush(self.larger, val)
        return self.larger[0] if self.larger else self.heap[0]

# Test cases
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3)) # Expected: 4
print(kthLargest.add(5)) # Expected: 5
print(kthLargest.add(10)) # Expected: 5
print(kthLargest.add(9)) # Expected: 8
print(kthLargest.add(4)) # Expected: 8

kthLargest = KthLargest(4, [7, 7, 7, 7, 8, 3])
print(kthLargest.add(2)) # Expected: 7
print(kthLargest.add(10)) # Expected: 7
print(kthLargest.add(9)) # Expected: 7
print(kthLargest.add(9)) # Expected: 8

kthLargest = KthLargest(2,[0])
print(kthLargest.add(-1)) # Expected: -1
print(kthLargest.add(1)) # Expected: 0
print(kthLargest.add(-2)) # Expected: 0
print(kthLargest.add(-4)) # Expected: 0
print(kthLargest.add(3)) # Expected: 1
