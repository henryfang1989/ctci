# question: implement an algorith to delete a node in the middle (i.e. any node but the first and
# last node, not necessarily the exact middle) of a singly linked list, given only access to that
# node
# Example
# Input: the node C from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f

def delete_middle_node(node):
    if not node or not node.next:
        return
    node.val, node.next.val == node.next.val, node.val
    node.next = node.next.next

from linked_list import Linkedlist

ll = Linkedlist([1,2,3,4])
delete_middle_node(ll.head)
ll.print_ll()
