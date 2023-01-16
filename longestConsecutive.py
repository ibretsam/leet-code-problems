def longestConsecutive(nums) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                curr = 1
                while num + curr in nums:
                    curr += 1
                longest = max(longest, curr)
        
        return longest
    
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))