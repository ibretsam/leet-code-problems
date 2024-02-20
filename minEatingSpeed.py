def minEatingSpeed(piles, h):
    k = min(piles)
    while True:
        count = 0
        leftover = 0
        for pile in piles:
            if pile > k:
                leftover += pile - k
            count += (pile // k)
            if pile % k != 0:
                count += 1
        if count <= h:
            print(k)
            return k
        elif leftover > h:
            k += leftover // h
            if leftover % h != 0:
                k += 1
        else:
            k += 1


piles = [3, 6, 7, 11]
h = 8
minEatingSpeed(piles, h)
