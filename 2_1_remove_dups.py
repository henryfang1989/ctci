# question: write code to remove diplicates from an unsorted linked list.
# follow up: how would you solve this problem if a temporary buffer is not allowed?

from linked_list import Linkedlist

def remove_dups(head):
	vals = set()
	prev_node = None
	while head:
		if head.val not in vals:
			vals.add(head.val)
		else:
			prev_node.next = head.next
		prev_node = head
		head = head.next

# time: O(n)
# space: O(n)

ll = Linkedlist([1,1,2,2,3])
remove_dups(ll.head)
ll.print_ll()

remove_dups(ll.head)
ll.print_ll()


# follow up
def remove_dups_2(head):
	cur = head
	while cur:
		runner = cur
		while runner.next:
			if cur.val == runner.next.val:
				runner.next = runner.next.next
			else:
				runner = runner.next
		cur = cur.next

# time: O(n^2)
# space: O(1)

ll = Linkedlist([1,1,2,2,3])
remove_dups(ll.head)
ll.print_ll()

remove_dups_2(ll.head)
ll.print_ll()
