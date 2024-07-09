import collections
def predictPartyVictory(senate):
    r_queue, d_queue = collections.deque(), collections.deque()

    for i, c in enumerate(senate):
        if c == "R":
            r_queue.append(i)
        else:
            d_queue.append(i)
    while r_queue and d_queue:
        if r_queue[0] < d_queue[0]:
            d_queue.popleft()
            r_queue.append(r_queue[0] + len(senate))
            r_queue.popleft()
        else:
            r_queue.popleft()
            d_queue.append(d_queue[0] + len(senate))
            d_queue.popleft()

    return "Radiant" if r_queue else "Dire"

print(predictPartyVictory("RD")) # "Radiant"
print(predictPartyVictory("RDD")) # "Dire"