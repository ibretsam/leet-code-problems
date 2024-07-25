"""
128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
import collections
def longestConsecutive(nums) -> int:
    # Solution #1: Check n - 1
    # nums = set(nums)
    # longest_streak = 0
    # for num in nums:
    #     if num - 1 not in nums:
    #         current_streak = 1
    #         while current_streak + num in nums:
    #             current_streak += 1
    #         longest_streak = max(longest_streak, current_streak)
    # return longest_streak

    # Solution #2: Using hashmap to check the next and previous value of current num
    nums = set(nums)
    hm = collections.defaultdict(int)
    max_streak = 0
    for num in nums:
        x = hm[num - 1]
        y = hm[num + 1]
        val = x + y + 1
        hm[num - x] = val
        hm[num + y] = val
        max_streak = max(max_streak, val)
    return max_streak
    
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))
nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))
nums = [9,1,4,7,3,-1,0,5,8,-1,6]
print(longestConsecutive(nums))