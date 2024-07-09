import math
def fullJustify(words, maxWidth):        
    remain = maxWidth
    res = [""]
    line_count = 0
    for word in words:
        if res[line_count] == "":
            if len(word) <= remain:
                res[line_count] += word
                remain -= len(word)
        else:
            if len(word) + 1 <= remain:
                res[line_count] += " " + word
                remain -= len(word) + 1
            else:                    
                line_count += 1
                res.append(word)
                remain = maxWidth - len(word)

    for i in range(len(res)):
        line = res[i]
        words = line.split()

        if i < len(res) - 1 and len(words) > 1:            
            total_spaces_needed = maxWidth - sum(len(word) for word in words)
            space_between_words, extra_spaces = divmod(total_spaces_needed, len(words) - 1)
            for j in range(extra_spaces):
                words[j] += ' '
            line = (' ' * space_between_words).join(words)
        else:
            spaces_to_add = maxWidth - len(line)            
            line += ' ' * spaces_to_add
        res[i] = line
    return res

# print(fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)) 
print(fullJustify(["What","must","be","acknowledgment","shall","be"], 16)) 
