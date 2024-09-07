"""
90. Subsets II
Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

def subsetsWithDup(nums):
    nums.sort()
    res = []
    n = len(nums)

    def backtrack(i, comb):
        if i == n:
            res.append(comb[:])
            return
        
        comb.append(nums[i])
        backtrack(i + 1, comb)
        comb.pop()

        while i + 1 < n and nums[i + 1] == nums[i]:
            i += 1
        backtrack(i + 1, comb)

    backtrack(0, [])
    return res

# Test cases
print(subsetsWithDup([1,2,2])) # [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(subsetsWithDup([0])) # [[],[0]]
