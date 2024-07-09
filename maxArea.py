"""
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Example 2:

Input: height = [1,1]
Output: 1
 
"""

def maxArea(height):
    l, r = 0, len(height) - 1
    res = 0
    while l < r:
        currArea = min(height[l], height[r]) * (r - l)
        res = max(res, currArea)
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return res
    
height = [1, 1]
print(maxArea(height))