# question: Given a circular linked list, implement an algorithm that returns the
# node at the begining of the loop
# Definition
# Circular linked list: A(corrupt) linked list in which a node's next pointer points to
# to an earlier node, so as to mae a loop in the linked list.
# Example
# Input: A -> B -> C -> D -> E -> C[the same C as earlier]
# Output: C

# Sol #1: find collision spot for fast and slow pointers, then set fast pointer to head and move
# fast and slow at 1 step each time, return the collision spot

def loop_detection(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next

    return fast

# time: O(n)
# space: O(1)

from linked_list import Node

n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n3

assert loop_detection(head).val == 3