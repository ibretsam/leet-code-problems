"""
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
"""
def searchRange(nums, target):
    if not nums:
        return [-1, -1]
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            i = j = m
            while i >= 0 and nums[i] == target:
                i -= 1
            while j < len(nums) and nums[j] == target:
                j += 1
            return [i + 1, j - 1]
    
    return [-1, -1]

# Test cases
print(searchRange([5,7,7,8,8,10], 8)) # [3,4]
print(searchRange([5,7,7,8,8,10], 6)) # [-1,-1]
print(searchRange([2, 2], 2)) # [0,1]