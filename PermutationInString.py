def checkInclusion(s1, s2) -> bool:
    start = 0
    smaller_str, longer_str = '', ''
    if len(s2) > len(s1):
        smaller_str = s1
        longer_str = s2
    else:
        smaller_str = s2
        longer_str = s1

    smaller_dict = {}
    for c in smaller_str:
        if c in smaller_dict:
            smaller_dict[c] += 1
        else:
            smaller_dict[c] = 1
    longer_dict = {}

    if len(smaller_str) == 1 and smaller_str in longer_str:
        return True

    for end in range(len(smaller_str), len(longer_str) + 1):
        for c in longer_str[start:end + 1]:
            print("")
            print(c)
            print("longer:")
            print(longer_dict)
            print("shorter: ")
            print(smaller_dict)
            check = False
            if len(longer_dict) == len(smaller_dict):
                for char in smaller_str:
                    if smaller_dict[char] != longer_dict[char]:
                        check = False
                        break
                    else:
                        check = True
                if check:
                    return True
                    
            if c in smaller_dict:
                if c in longer_dict:
                    longer_dict[c] += 1
                    if longer_dict[c] > smaller_dict[c]:
                        start += 1
                        longer_dict = {}
                        break
                    check = False
                    if len(longer_dict) == len(smaller_dict):
                        for char in smaller_str:
                            if smaller_dict[char] != longer_dict[char]:
                                check = False
                                break
                            else:
                                check = True
                        if check:
                            return True
                else:
                    longer_dict[c] = 1
            else:
                longer_dict = {}
                start += 1
                break

    return False


print(checkInclusion('adc', 'dcda'))
