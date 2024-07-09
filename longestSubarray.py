def longestSubarray(nums) -> int:
    max_length = 0
    k = 1
    l = 0
    for r, num in enumerate(nums):
        if num == 0:
            k -= 1
        if k < 0:
            if nums[l] == 0:
                k += 1
            l += 1

        max_length = max(max_length, r - l)

    return max_length

print(longestSubarray([0,1,1,1,0,1,1,0,1]))  # 5
print(longestSubarray([1, 1,0,1]))  # 3
print(longestSubarray([1,1,1]))  # 2
print(longestSubarray([1, 0,0,0,0]))  # 1