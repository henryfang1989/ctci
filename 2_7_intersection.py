# question: given two (singly) linked lists, determine if the two lists intersect.
# return the intersecting node. Note that the intersection is defined based on reference,
# not value. That is, if the kth node of the first linked list is the exact same node (by reference)
# as the jth node of the second linked list, then they are intersecting.

# Sol #1: find the diff in length and move the diff steps in longer linked list.
# then compare the nodes in two linked lists one by one

def intersection(head1, head2):
    len1 = length_of(head1)
    len2 = length_of(head2)
    if len1 > len2:
        long, short = head1, head2
    else:
        long, short = head2, head1

    diff = abs(len1 - len2)
    while diff:
        long = long.next
        diff -= 1

    while long:
        if long == short:
            return True
        long = long.next
        short = short.next
    return False

def length_of(head):
    cnt = 0
    while head:
        cnt += 1
        head = head.next
    return cnt

# time: O(max(m+n))
# space: O(1)


# Note: we cannot compare from the tail of linked lists. Because tails of linked lists maybe forked.
# Then the recursive way to find from tails of linked list is same as from the beginning of linked lists.

from linked_list import Node

n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
head1 = n1
head2 = n3
n1.next = n2
n2.next = n4
n4.next = n5
n3.next = n4
assert intersection(head1, head2)