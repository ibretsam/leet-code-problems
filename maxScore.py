nums1 = [4, 2, 3, 1, 1, 7, 9, 8]
nums2 = [7, 5, 10, 9, 6, 5, 4, 2]
k = 3
nums1 = [x for _, x in sorted(zip(nums2, nums1))]
nums2.sort()
curr_max = []
print(nums1)
print(nums2)
for i, num in enumerate(nums2[:len(nums2) - k + 1]):
    curr_sum = 0
    import copy
    test2 = copy.deepcopy(nums1)
    curr_sum += test2[i]
    test2.pop(i)
    for _ in range(k - 1):
        curr_sum += max(test2)
        test2.remove(max(test2))
    curr_prod = curr_sum * num
    curr_max.append(curr_prod)

print(curr_max)
