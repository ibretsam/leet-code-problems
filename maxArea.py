def maxArea(height):
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            amount = min(height[l], height[r]) * (r - l)
            while height[l] < height[l + 1]:
                r -= 1
            while height[r] < height[r - 1]:
                l += 1
                
            l += 1
            r -= 1
            res = max(amount, res)
        return res
    
height = [1,3,2,5,25,24,5]
print(maxArea(height))