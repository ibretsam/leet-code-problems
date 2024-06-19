def removeDuplicates(nums) -> int:
    k = 0
    for i, num in enumerate(nums):
        if i < len(nums) - 1 and nums[i + 1] != num:
            k += 1
            nums[k] = nums[i + 1]
        elif i == len(nums) - 1:
            if nums[k] != num:
                k += 1
                nums[k] = num
    return k

# print(removeDuplicates([1, 1, 2])) # 2
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])) # 5