def candy(ratings):
    res = [0] * len(ratings)
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            res[i] = res[i - 1] + 1
    
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and res[i] <= res[i + 1]:
            res[i] = res[i + 1] + 1
    return res

# print(candy([1,0,2])) # 5
# print(candy([1,2,2]))
print(candy([3,2,1,5,9]))
print(candy([2,3,5,1,4]))
print(candy([1,2,5,4,3]))
print(candy([1,2,2,4,5]))