# question: write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition elements x can appear aywhere in the "right partition", it does not need to appear between the left and right partitions.

# Example
# Input: 3->5->8->5->10->2->1 (partition = 5)
# Output: 3->1->2->10->5->5->8

from linked_list import Linkedlist, print_linkedlist

def partition(head, par):
	small = Linkedlist([])
	large = Linkedlist([])
	while head:
		next = head.next
		head.next = None
		if head.val >= par:
			large.append(head.val)
		else:
			small.append(head.val)

		head = next

	# concatnate two linked lists
	t = small.head
	if not t:
		return large
	while t.next:
		t = t.next
	t.next = large.head
	return small

# time: O(n)
# space: (1)

ll = Linkedlist([1,5,2,4,3])
partition(ll.head,3).print_ll()

# use the head as parition node to seperate the nodes
def partition2(node, par):
	head = tail = node

	while node:
		next = node.next
		if node.val < par:
			node.next = head
			head = node
		else:
			tail.next = node
			tail = node
		node = next
	tail.next = None

	return head

# time: O(n)
# space: O(1)

ll = Linkedlist([1,5,2,4,3])
new_head  = partition2(ll.head,3)
print_linkedlist(new_head)



