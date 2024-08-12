"""
138. Copy List with Random Pointer
A linked list of length n is given such that each node contains an additional random pointer, 
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node. Both the 
next and random pointer of the new nodes should point to new nodes in the copied list such that 
the pointers in the original list and copied list represent the same list state. None of the 
pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for 
the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented 
as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or 
null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 

Constraints:
0 <= n <= 1000
-104 <= Node.val <= 10^4
Node.random is null or is pointing to some node in the linked list.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        # Create a mapping of nodes to their positions
        node_to_pos = {}
        current = self
        pos = 0
        while current:
            node_to_pos[current] = pos
            current = current.next
            pos += 1

        # Build the string representation
        res = []
        current = self
        while current:
            random_pos = node_to_pos[current.random] if current.random else None
            res.append([current.val, random_pos])
            current = current.next
        return str(res)


def copyRandomList(head):
    new_nodes = {None : None}
    curr = head
    while curr:
        copy = Node(curr.val)
        new_nodes[curr] = copy
        curr = curr.next

    curr = head
    while curr:
        copy = new_nodes[curr]
        copy.next = new_nodes[curr.next]
        copy.random = new_nodes[curr.random]
        curr = curr.next
    return new_nodes[head]

# Test Cases
# [[7,null],[13,0],[11,4],[10,2],[1,0]]
head = Node(7)
head.next = Node(13)
head.next.next = Node(11)
head.next.next.next = Node(10)
head.next.next.next.next = Node(1)
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head
print(copyRandomList(head)) # [[7,null],[13,0],[11,4],[10,2],[1,0]]


# [[1,1],[2,1]]
head = Node(1)
head.next = Node(2)
head.random = head.next
head.next.random = head.next
print(copyRandomList(head)) # [[1,1],[2,1]]

# [[3,null],[3,0],[3,null]]
head = Node(3)
head.next = Node(3)
head.next.next = Node(3)
head.random = None
head.next.random = head
head.next.next.random = None
print(copyRandomList(head)) # [[3,null],[3,0],[3,null]]
