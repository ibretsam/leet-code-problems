"""
219. Contains Duplicate II
Given an integer array nums and an integer k, return true if there are two distinct indices i and j 
in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

def containsNearbyDuplicate(nums, k):

    # 1. Using Hashmap
    freq = {}
    for i, num in enumerate(nums):
        if num in freq and abs(i - freq[num]) <= k:
            return True        
        freq[num] = i

    # 2. Using Sliding Window:
    # if k == 0:
    #     return False
    # window = set()
    # for i, num in enumerate(nums):
    #     if num in window:
    #         return True
    #     window.add(num)
    #     if len(window) > k:
    #         window.remove(nums[i - k])

    return False

print(containsNearbyDuplicate([1,2,3,1], 3)) # True
print(containsNearbyDuplicate([1,0,1,1], 1)) # True
print(containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False