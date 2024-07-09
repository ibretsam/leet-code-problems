def successfulPairs(spells, potions, success):
    pairs = []
    potions.sort()
    for spell in spells:         
        i, j = 0, len(potions) - 1
        while i <= j:
            m = (i + j) // 2
            if spell * potions[m] < success:
                i = m + 1
            else:
                j = m - 1
        pairs.append(len(potions) - i)

    return pairs

print(successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))
print(successfulPairs([3, 1, 2], [8, 5, 8], 16))
print(successfulPairs([15, 8, 19], [38, 36, 23], 328))