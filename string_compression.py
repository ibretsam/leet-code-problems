def compress(chars):
    i = j = 0
    while i < len(chars):
        char = chars[i]
        count = 0
        while i < len(chars) and chars[i] == char:
            i += 1
            count += 1
        chars[j] = char
        j += 1
        if count > 1:
            for digit in str(count):
                chars[j] = digit
                j += 1
    return chars[:j]

print(compress(['a', 'a', '2', '2', '2']))
print(compress(["a","a","b","b","c","c","c"]))
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(compress(["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"]))
print(compress(["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]))