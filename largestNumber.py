"""
179. Largest Number
Given a list of non-negative integers nums, arrange them such that they form the largest number 
and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330" 

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 10^9
"""
from functools import cmp_to_key

def largestNumber(nums) -> str:
    # Convert numbers to strings
    nums_str = list(map(str, nums))
    
    # Sort using the custom comparator defined as a lambda function
    nums_str.sort(key=cmp_to_key(lambda x, y: 1 if x + y < y + x else -1))
    
    # Join the sorted numbers
    result = ''.join(nums_str)
    
    # Handle the case where the result is "0"
    if result[0] == '0':
        return '0'
    
    return result

print(largestNumber([3,30,34,5,9])) # 9534330