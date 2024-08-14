"""
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head. 

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1] 

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
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
    
def removeNthFromEnd(head, n):

    # 1 
    # dummy = ListNode(0, head)    
    # list_length = 0
    # while head:
    #     head = head.next
    #     list_length += 1
    # if list_length == 1 and n == 1:
    #     return None
    # head = dummy.next
    # pos = 1
    # actual_pos = list_length - n
    # if actual_pos == 0:
    #     return head.next
    # while head and pos != actual_pos:        
    #     head = head.next
    #     pos += 1
    # head.next = head.next.next
    # return dummy.next

    # 2
    dummy = ListNode(0, head)
    first = dummy
    second = dummy

    for _ in range(n + 1):
        first = first.next
    
    while first:
        first = first.next
        second = second.next
    
    second.next = second.next.next
    return dummy.next
    
# Test Cases
# head = [1,2,3,4,5], n = 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(removeNthFromEnd(head, 2)) # [1,2,3,5]

# head = [1], n = 1
head = ListNode(1)
print(removeNthFromEnd(head, 1)) # []

# head = [1,2], n = 2
head = ListNode(1)
head.next = ListNode(2)
print(removeNthFromEnd(head, 2)) # [2]

