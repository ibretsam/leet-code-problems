from copy import deepcopy
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val) + " -> " + str(self.next)    

def pairSum(head):
    first = deepcopy(head)
    max_sum = 0
    last = head
    prev = None
    while last:
        _next = last.next
        last.next = prev
        prev = last
        last = _next    

    while first.next is not None:
        max_sum = max(first.val + prev.val, max_sum)
        first = first.next
        prev = prev.next
    
    return max_sum

print(pairSum(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
