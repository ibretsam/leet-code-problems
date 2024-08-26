"""
25. Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return 
the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain 
as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 
Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
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
    
def reverseKGroup(head, k):
    dummy = ListNode(0)
    curr = head
    i = 1
    ktail = None
    while True:
        while i != k:
            if curr and curr.next:
                curr = curr.next
                i += 1
            else:
                break
        if not curr:
            break
        if i == k:
            next = curr.next
            curr.next = None
            new_head = reverse(head)
            curr = new_head
            if ktail:
                ktail.next = curr
            while curr.next:
                curr = curr.next
            ktail = curr
            ktail.next = None
            if not dummy.next:
                dummy.next = new_head
            i = 1
            head = next
            curr = head
        else:
            ktail.next = head
            break

    return dummy.next


def reverse(head):
    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
    
# Test cases
# [1,2,3,4,5], k = 2
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# print(reverse(head))
print(reverseKGroup(head, 2)) # [2,1,4,3,5]

# # [1,2,3,4,5], k = 3
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(reverseKGroup(head, 3)) # [3,2,1,4,5]