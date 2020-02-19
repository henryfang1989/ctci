# question: you have two numbers represented by a linked list,
# where each node contains a single digit. The digits are stored in reverese order,
# such that the 1's digit is at the head of the list.
# write a function that adds the two numbers and returns the sum as a linked list

# Example
# Input: (7->1->6) + (5->9->2),that is 617 + 295
# Output: (2->1->9) that is 912

# Follow up
# Suppose the difits are stored in forward order, Repeat the above problem
# Input: 6->1->7 + 2->9->5. that is 617+295
# Output: 9->1->2 that is 912

from utils import Linkedlist, print_linkedlist, Node

def sum_lists(head1, head2):
	dummy = tmp = Node(-1)
	c = 0
	while head1 and head2:
		s = head1.val + head2.val + c
		d = s % 10
		c = s / 10
		tmp.next = Node(d)
		tmp = tmp.next
		head1 = head1.next
		head2 = head2.next

	while head1:
		s = head1.val + c
		d = s % 10
		c = s / 10
		tmp.next = Node(d)
		tmp = tmp.next
		head1 = head1.next

	while head2:
		s = head2.val + c
		d = s % 10
		c = s / 10
		tmp.next = Node(d)
		tmp = tmp.next
		head2 = head2.next

	if c:
		tmp.next = Node(c)

	return dummy.next

# time: O(max(N, M))
# space: O(max(N, M))

ll1 = Linkedlist([1,2,3,4,5])

ll2 = Linkedlist([4,5,6,7])

print ll1
print ll2
print_linkedlist(sum_lists(ll1.head, ll2.head))


# follow up
# solution 1: reverse the linked list and add two number and reverse the result

# solution 2: use recursive way to do it.
# 1. padding the short linked list with zeros in the beginning of list
# 2. use recursive call to sum up

def sum_lists2(head1, head2):
	head1, head2 = padding_zero(head1, head2)
	c, head = dfs_helper(head1, head2)
	if c:
		new_node = Node(c)
		new_node.next = head
		head = new_node
	return head
# time: O(max(m, n))
# space: O(max(m, n))
# m, n are two linked list lengths


# padding zeros on the short linked list
def padding_zero(head1, head2):
	t1, t2 = head1, head2
	while t1 or t2:
		if not t1 and not t2:
			break
		if not t1:
			new_node = Node(0)
			new_node.next = head1
			head1 = new_node
		if not t2:
			new_node = Node(0)
			new_node.next = head2
			head2 = new_node
		if t1:
			t1 = t1.next
		if t2:
			t2 = t2.next
	return head1, head2
# time: O(max(m, n))
# space: O(abs(m-n))

def dfs_helper(head1, head2):
	# head1 and head2 have the same length
	# so we only need to check head1
	if not head1.next:
		s = head1.val + head2.val
		c = s / 10
		r = s % 10
		return c, Node(r)
	else:
		c, next_node = dfs_helper(head1.next, head2.next)
		s = c + head1.val + head2.val
		c = s / 10
		r = s % 10
		cur_node = Node(r)
		cur_node.next = next_node
		return c, cur_node

# time: O(max(m, n))
# space: O(max(m, n))

print("Follow up")
ll1 = Linkedlist([1,2,3,4,5])
ll2 = Linkedlist([4,5,6,7])

print ll1
print ll2
print_linkedlist(sum_lists2(ll1.head, ll2.head))
