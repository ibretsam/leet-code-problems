def longestCommonPrefix(strs) -> str:
    if "" in strs:
        return ""
    if len(strs) == 1 or all(i == strs[0] for i in strs):
        return strs[0]             
    found = False
    current_index = 0
    current_prefix = strs[0][current_index]
    while not found:            
        for word in strs[1:]:
            if current_index < len(word):
                if word[:current_index + 1] != current_prefix:
                    found = True
                    break
            else:
                if word == current_prefix:
                    return word
                else:
                    return current_prefix[:-1]
        if found:
            current_prefix = current_prefix[: -1]
        else:                 
            current_index += 1
            if current_index < len(strs[0]):
                current_prefix += strs[0][current_index]
            else:
                if current_prefix == strs[0]:
                    return strs[0]
                else:
                    return ""
    return current_prefix 

print(longestCommonPrefix(["babb","caa"])) # ""