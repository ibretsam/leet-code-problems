"""
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = []
        while self:
            res.append(self.val)
            self = self.next
        return str(res)

def mergeTwoLists(list1, list2):
    res = ListNode()
    curr = res
    while list1 and list2:
        if list1.val > list2.val:
            curr.next = list2
            list2 = list2.next
        else:
            curr.next = list1
            list1 = list1.next
        curr = curr.next

    if list1:
        curr.next = list1
    else:
        curr.next = list2
    return res.next


        


# Test cases
# 1 -> 2 -> 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# 1 -> 1 -> 2 -> 3 -> 4 -> 4
print(mergeTwoLists(list1, list2)) # [1,1,2,3,4,4]

# []
list1 = None
list2 = None
print(mergeTwoLists(list1, list2)) # []

# [0]
list1 = None
list2 = ListNode(0)
print(mergeTwoLists(list1, list2)) # [0]