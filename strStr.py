def strStr(haystack, needle):
    if not needle:
        return 0
    if needle not in haystack:
        return -1
    return haystack.index(needle)

print(strStr("hello", "ll")) # 2
print(strStr("sadbutsad", "sad")) # 0