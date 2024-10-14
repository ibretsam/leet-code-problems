"""
23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
 
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"

def mergeKLists(lists):
    def merge(left, right):
        merged = ListNode(0)
        curr = merged
        while left or right:
            if not left:
                curr.next = right
                right = right.next
            elif not right:
                curr.next = left
                left = left.next
            else:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
            curr = curr.next
        
        return merged.next
    if not lists:
        return

    while len(lists) > 1:
        l1, l2 = lists[0], lists[1]
        merged = merge(l1, l2)
        lists.append(merged)
        lists = lists[2:]
    
    return lists[0]

# Test cases
# [[1,4,5],[1,3,4],[2,6]]
# 1 -> 4 -> 5
# 1 -> 3 -> 4
# 2 -> 6
lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
print(mergeKLists(lists)) # 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6