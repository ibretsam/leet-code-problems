"""
82. Remove Duplicates from Sorted List II
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the 
original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
 
Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
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

def deleteDuplicates(head):
    if not head:
        return None
    dummy = ListNode(0, head)
    prev, curr = dummy, head    
    while curr and curr.next:
        next = curr.next
        if next and curr.val != next.val:
            prev = prev.next
            curr = curr.next
        else:
            while next and curr.val == next.val:                
                curr = curr.next
                next = curr.next
            curr = next
            prev.next = curr            
    return dummy.next


# Test cases
head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
print(deleteDuplicates(head)) # [1,2,5]

head = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
print(deleteDuplicates(head)) # [2,3]

head = ListNode(1, ListNode(1))
print(deleteDuplicates(head)) # []