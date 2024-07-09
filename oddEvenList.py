class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val) + " -> " + str(self.next)

def oddEvenList(head):
    while not head or not head.next:
        return head
    odd, even = ListNode(), ListNode()
    curr = head
    while curr:
        last_odd = odd
        last_even = even
        while last_odd.next:
            last_odd = last_odd.next
        while last_even.next:
            last_even = last_even.next
        last_odd.next = curr
        last_even.next = curr.next
        curr = curr.next.next if curr.next else None
    

    return odd

print(oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))) # 1 -> 3 -> 5 -> None, 4 -> None
print(oddEvenList(ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7))))))))) # 2 -> 1 -> 3 -> 5 -> 7 -> None, 6 -> 4 -> None
