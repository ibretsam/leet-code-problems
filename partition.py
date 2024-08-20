"""
86. Partition List
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes 
greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
 
Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
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
	
def partition(head, x):
	if not head:
		return head
	smaller_head, larger_head = ListNode(0), ListNode(0)
	smaller, larger = smaller_head, larger_head
	curr = head
	while curr:
		if curr.val >= x:
			larger.next = curr
			larger = larger.next
		else:
			smaller.next = curr
			smaller = smaller.next
		curr = curr.next	
	smaller.next = larger_head.next
	larger.next = None

	return smaller_head.next
	
	

# [1,4,3,2,5,2], x = 3
head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
print(partition(head, 3)) # [1,2,2,4,3,5]

# [2,1], x = 2
head = ListNode(2, ListNode(1))
print(partition(head, 2)) # [1,2]