"""
61. Rotate List
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 
Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9
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
	
def rotateRight(head, k):
	if not head:
		return head
	
	tail, pos = head, 1
	while tail.next:
		pos += 1
		tail = tail.next
	
	k = k % pos
	if k == 0:
		return head
	curr = head
	for _ in range(pos - k - 1):
		curr = curr.next
	new_head = curr.next
	curr.next = None
	tail.next = head

	return new_head


# [1,2,3,4,5], k = 2
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(rotateRight(head, 2)) # [4,5,1,2,3]

# [0,1,2], k = 4
head = ListNode(0, ListNode(1, ListNode(2)))
print(rotateRight(head, 4)) # [2,0,1]

# [1], k = 1
head = ListNode(1)
print(rotateRight(head, 1)) # 1

# [1, 2], k = 1
head = ListNode(1, ListNode(2))
print(rotateRight(head, 1)) # [2, 1]