"""
846. Hand of Straights
Alice has some number of cards and she wants to rearrange the cards into groups so that 
each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer
groupSize, return true if she can rearrange the cards, or false otherwise.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

Constraints:
1 <= hand.length <= 10^4
0 <= hand[i] <= 10^9
1 <= groupSize <= hand.length
"""
import heapq, collections
def isNStraightHand(hand, groupSize) -> bool:
    if len(hand) % groupSize:
        return False
    
    count = collections.Counter(hand)
    heap = list(count.keys())
    heapq.heapify(heap)    

    while heap:
        smallest = heap[0]

        for card in range(smallest, smallest + groupSize):
            if card not in count:
                return False

            count[card] -= 1
            if count[card] == 0:
                if card != heap[0]:
                    return False
                heapq.heappop(heap)
    return True



# Test Cases
print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3)) # True
print(isNStraightHand([1,2,3,4,5], 4)) # False
print(isNStraightHand([1,2,3,4,5], 5)) # True
print(isNStraightHand([1,2,3,4,5], 1)) # True
print(isNStraightHand([1,1,2,2,3,3], 2)) # False
print(isNStraightHand([1,2,3,4,5,6], 2)) # True