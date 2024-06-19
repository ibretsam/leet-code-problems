def dailyTemperatures(temperatures):
    answer = []
    for i, temp in enumerate(temperatures):
        j = i + 1
        curr_count = 0
        if j < len(temperatures) - 1 and temperatures[j] > temp:
            curr_count += 1                
        else:            
            while j < len(temperatures) - 1 and temperatures[j] < temp:                
                j += 1
            if j < len(temperatures) - 1 and temperatures[j] > temp:
                curr_count += j - i
        answer.append(curr_count)

    return answer

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])) # [1, 1, 4, 2, 1, 1, 0, 0]