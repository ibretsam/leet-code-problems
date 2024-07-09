import heapq
def totalCost(costs, k, candidates) -> int:
    cost = 0
    i, j = 0, len(costs) - 1
    left_heap, right_heap = [], []
    for _ in range(k):
        while (len(left_heap) < candidates and i <= j):
            heapq.heappush(left_heap, costs[i])
            i += 1
        while (len(right_heap) < candidates and i <= j):
            heapq.heappush(right_heap, costs[j])
            j -= 1
        if not left_heap:
            cost += heapq.heappop(right_heap)
        elif not right_heap:
            cost += heapq.heappop(left_heap)
        elif left_heap[0] <= right_heap[0]:
            cost += heapq.heappop(left_heap)
        else:
            cost += heapq.heappop(right_heap)
    return cost


print(totalCost([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4)) # 11
print(totalCost([1, 2, 4, 1], 3, 3)) # 4
print(totalCost([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], 11, 2))
print(totalCost([50,80,34,9,86,20,67,94,65,82,40,79,74,92,84,37,19,16,85,20,79,25,89,55,67,84,3,79,38,16,44,2,54,58], 7, 12)) # 95