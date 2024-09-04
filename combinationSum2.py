"""
40. Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations 
in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
def combinationSum2(candidates, target):
    candidates.sort()
    res = []

    def backtrack(index, curr_sum, curr_res):
        if curr_sum == target:
            res.append(curr_res[:])
        if curr_sum >= target:
            return
        
        prev = -1
        for i in range(index, len(candidates)):
            if curr_sum + candidates[i] <= target:
                if candidates[i] == prev:
                    continue
                curr_res.append(candidates[i])
                backtrack(i + 1, curr_sum + candidates[i], curr_res)
                curr_res.pop()
                prev = candidates[i]

    backtrack(0, 0, [])
    return res

# Test cases
print(combinationSum2([10,1,2,7,6,1,5], 8)) # [[1,1,6],[1,2,5],[1,7],[2,6]]
print(combinationSum2([2,5,2,1,2], 5)) # [[1,2,2],[5]]