class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val) + " -> " + str(self.next)    
    
class Solution:
    def deleteMiddle(head):
        if not head or not head.next:
            return None
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        middle = length // 2
        count, prev = 0, None
        curr = head
        while curr:
            count += 1
            prev = curr
            curr = curr.next
            if count == middle:
                prev.next = curr.next

        return head
    
    print(deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))) # 1 -> 2 -> 4 -> 5
    print(deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))) # 1 -> 2 -> 4