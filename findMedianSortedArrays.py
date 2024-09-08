"""
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""
def findMedianSortedArrays(nums1, nums2):
    n, m = len(nums1), len(nums2)
    total_length = n + m
    half_length = total_length // 2

    if m < n:
        return findMedianSortedArrays(nums2, nums1)
    
    l, r = 0, n - 1
    while True:
        m1 = (l + r) // 2
        m2 = half_length - m1 - 2

        left_1 = nums1[m1] if m1 >= 0 else float('-inf')
        right_1 = nums1[m1 + 1] if (m1 + 1) < n else float('inf')
        left_2 = nums2[m2] if m2 >= 0 else float('-inf')
        right_2 = nums2[m2 + 1] if (m2 + 1) < m else float('inf')

        if left_1 <= right_2 and left_2 <= right_1:
            if total_length % 2:
                return min(right_1, right_2)
            return (max(left_1, left_2) + min(right_1, right_2)) /2
        elif left_1 > right_2:
            r = m1 - 1
        else:
            l = m1 + 1



"""
[1,2,3,4,5,6]
[1,2,3,4,5,6,7,8]
"""

# Test cases
print(findMedianSortedArrays([1,3], [2])) # 2.00000
print(findMedianSortedArrays([1,2], [3,4])) # 2.50000