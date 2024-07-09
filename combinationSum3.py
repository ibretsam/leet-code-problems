def combinationSum3(k: int, n: int):
    res = []

    def backtrack(i, curr, target):
        if len(curr) == k and target == 0:            
            res.append(curr)

        for num in range(i + 1, 10):
            if num <= target:
                backtrack(num, curr + [num], target - num)

    backtrack(0, [], n)
    return res


print(combinationSum3(3, 7))
print(combinationSum3(3, 9))