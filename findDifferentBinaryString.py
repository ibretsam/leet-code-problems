"""
1980. Find Unique Binary String
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n 
that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

Constraints:
    n == nums.length
    1 <= n <= 16
    nums[i].length == n
    nums[i] is either '0' or '1'.
    All the strings of nums are unique.
"""
def findDifferentBinaryString(nums) -> str:
    """
    Time complexity: O(n * 2^n)
    Space complexity: O(n) for the recursion stack
    """
    res = [""]
    n = len(nums)
    def backtrack(curr_str):
        if len(curr_str) == n and curr_str not in nums:
            res[0] = curr_str
            return True
        if backtrack(curr_str + "0"):
            return True
        return backtrack(curr_str + "1")
    
    backtrack("")
    return res[0]

def findDifferentBinaryString(nums) -> str:
    """
    Time complexity: O(n * 2^n) - string concatenation is O(n), and we might need to try all 2^n combinations
    Space complexity: O(n + k) where k is the size of nums_set
    - O(n) for recursion stack depth
    - O(k) for storing the set of strings
    """
    nums_set = set(nums)
    n = len(nums)

    def backtrack(curr_str):
        if len(curr_str) == n:
            return curr_str if curr_str not in nums_set else None
        
        res =  backtrack(curr_str + "0")
        if res:
            return res
        
        return backtrack(curr_str + "1")
    return backtrack("")

print(findDifferentBinaryString(["01", "10"])) # 11