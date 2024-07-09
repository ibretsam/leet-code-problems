def maxVowels(s, k):
    vowels = 'aeiou'
    s = list(s)
    vowelCount = 0
    currSub = s[:k]
    currMax = 0
    for c in currSub:
        if c in vowels:
            vowelCount += 1
            currMax = max(currMax, vowelCount)
    l, r = 0, k - 1
    while r < len(s):
        l += 1
        r += 1
        if r == len(s):
            break
        currSub = currSub[1:]
        currSub.append(s[r])
        if s[l - 1] in vowels:
            vowelCount -= 1
        if s[r] in vowels:
            vowelCount += 1
        currMax = max(currMax, vowelCount)
    return currMax


print(maxVowels("ramadan", 2))  # 3
