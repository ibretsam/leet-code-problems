from collections import Counter
def closeStrings(word1, word2) -> bool:
    count1 = Counter(word1)
    count2 = Counter(word2)
    return set(count1.keys()) == set(count2.keys()) and sorted(count1.values()) == sorted(count2.values())


print(closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"))  # False
print(closeStrings("a", "aa")) # False
print(closeStrings("cabbba", "abbccc")) # True