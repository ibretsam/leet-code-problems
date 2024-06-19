def numTilings(n: int, memo={}) -> int:
    if n in memo:
        return memo[n]
    if n < 3:
        result = n
    elif n < 5:
        result = 2 * (numTilings(n - 1, memo)) + 1
    else:
        result = (2 * (numTilings(n - 1, memo)) +
                  numTilings(n - 3, memo)) % (10**9 + 7)
    memo[n] = result
    return result

print(numTilings(24))
print(numTilings(25))
print(numTilings(26))
print(numTilings(27))  # 867954037
print(numTilings(28))  # 914332884
print(numTilings(29))  # 222194076
print(numTilings(30))  # 312342182
print(numTilings(40))
print(numTilings(50))
print(numTilings(60))
