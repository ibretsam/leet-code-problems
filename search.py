def search(nums, target):
    if not nums:
            return -1
    mid = len(nums) // 2
    if target == nums[mid]:
        return mid
    elif target < nums[mid]:
        return search(nums[:mid], target)
    else:
        right_search = search(nums[mid + 1:], target)
        if right_search == -1:
            return -1
        else:
            return right_search + mid + 1
        

nums, target = [-1,0,3,5,9,12,15,17,19,22,25,30,50], 12
print(search(nums, target))