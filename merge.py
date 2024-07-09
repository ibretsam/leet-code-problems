def merge(nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(m, m + n):
        nums1[i] = nums2[i - n]
    nums1.sort()
    print(nums1)

merge([1,2,4,5,6,0], 5, [3], 1) # [1,2,3,4,5,6]

