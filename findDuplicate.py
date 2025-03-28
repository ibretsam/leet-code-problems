"""
287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and using only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3

Constraints:
1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 
Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""

# Time complexity: O(n)
# Space complexity: O(1)
def findDuplicate(nums) -> int:
    for i in range(len(nums)):
        idx = abs(nums[i])
        if nums[idx] < 0:
            return idx
        nums[idx] = -nums[idx]

# Time complexity: O(n)
# Space complexity: O(1)
def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    
    return ptr1

# Test cases
print(findDuplicate([1,3,4,2,2])) # Expected: 2
print(findDuplicate([3,1,3,4,2])) # Expected: 3
print(findDuplicate([1,1])) # Expected: 1