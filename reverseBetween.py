"""
92. Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list. 

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
 
Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 
Follow up: Could you do it in one pass?
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
    
def reverseBetween(head, left: int, right: int):
    if not head or left == right:
        return head
    prev, curr, pos = None, head, 1
    prevList = None
    h = head
    while curr:
        if pos < left or pos > right:
            prev = curr
            curr = curr.next
        else:
            if pos == left:
                prevList = prev
                prev = curr
                curr = curr.next
                prev.next = None
            elif pos == right:
                if prevList != None:
                    first = prevList.next
                    prevList.next = curr
                    first.next = curr.next
                    curr.next = prev
                else:
                    next = curr.next
                    if next != None:
                        curr_prev = prev
                        while curr_prev.next:
                            curr_prev = curr_prev.next
                        curr_prev.next = next
                    curr.next = prev
                    prev = curr
                    h = curr
                    curr = next                    
            else:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
        pos += 1
    return h

# head = [1,2,3,4,5], left = 2, right = 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
left = 2
right = 4
print(reverseBetween(head, left, right)) # [1,4,3,2,5]

# head = [5], left = 1, right = 1
head = ListNode(5)
left = 1
right = 1
print(reverseBetween(head, left, right)) # [5]

# head = [3,5], left = 1, right = 2
head = ListNode(3)
head.next = ListNode(5)
left = 1
right = 2
print(reverseBetween(head, left, right)) # [5,3]

# head = [1,2,3], left = 1, right = 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
left = 1
right = 2
print(reverseBetween(head, left, right)) # [2,1,3]

# head = [1,2,3], left = 1, right = 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
left = 1
right = 3
print(reverseBetween(head, left, right)) # [3,2,1]

# head = [3,5], left = 1, right = 1
head = ListNode(3)
head.next = ListNode(5)
left = 1
right = 1
print(reverseBetween(head, left, right)) # [3,5]

# head = [1,2,3,4], left = 1, right = 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
left = 1
right = 3
print(reverseBetween(head, left, right)) # [3,2,1,4]