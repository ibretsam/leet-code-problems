"""
148. Sort List
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is in the range [0, 5 * 10^4].
-105 <= Node.val <= 105

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
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

def sortList(head):
    if not head or not head.next:
        return head
    list1, list2 = split(head)
    l = sortList(list1)
    r = sortList(list2)
    return merge(l, r)

def split(lst):
    slow, fast = lst, lst.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    mid = slow.next
    slow.next = None
    return lst, mid

def merge(list1, list2):
    merged_list = ListNode()
    curr = merged_list
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    
    if list1:
        curr.next = list1
    if list2:
        curr.next = list2
    
    return merged_list.next

# Test cases
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
print(sortList(head)) # Expected output: [1,2,3,4]

head = ListNode(-1)
head.next = ListNode(5)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(0)
print(sortList(head)) # Expected output: [-1,0,3,4,5]

head = None
print(sortList(head)) # Expected output: []