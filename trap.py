"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""

def trap(height):
    stack = []
    res = 0
    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            lowest = stack.pop()

            if not stack:
                break

            distance = i - stack[-1] - 1
            bounded_height = min(h, height[stack[-1]]) - height[lowest]
            res += bounded_height * distance
        stack.append(i)

    return res




# print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(trap([4,2,0,3,2,5])) # 9
# print(trap([4,2,3])) # 1
# print(trap([4,2,3,1])) # 1
print(trap([4,2,3,1,2])) # 2
 