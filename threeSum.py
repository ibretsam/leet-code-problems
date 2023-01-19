def threeSum(nums):
        nums.sort()
        res = set()
        for i, num in enumerate(nums):
            if i == 0:
                l = i + 1
            else:
                l = i - 1
            r = len(nums) - 1
            while l < r:
                if nums[l] == num:
                    l += 1
                if nums[r] == num:
                    r -= 1
                if nums[l] + nums[r] > num:
                    r -= 1
                elif nums[l] + nums[r] < num:
                    l += 1
                else: 
                    triplet = [num, nums[l], nums[r]]
                    res.add(tuple(triplet))
                
        return res
    
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))