# question: implement a function to check if a linked list is palindrome

# solution #1
# resevse the linked list and compare two linked lists

# solution #2
# use the recursive way compare the node in tail and head

# solution #3
# find the middle node and compare by from middle, but still need the recursive call

from linked_list import Node, Linkedlist
def reverse_compare(head):
    dummy = Node(-1)
    tmp = head
    while tmp:
        new_node = Node(tmp.val)
        new_node.next = dummy.next
        dummy.next = new_node
        tmp = tmp.next
    head2 = dummy.next
    return compare(head, head2)

def compare(head1, head2):
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1, head2 = head1.next, head2.next
    return not head1 and not head2

# time: O(n)
# space: O(n)

print "reverse and compare"
l1 = Linkedlist([1,2,1])
assert reverse_compare(l1.head)
l1 = Linkedlist([1,2,2])
assert not reverse_compare(l1.head)


def iterative(head):
    stack = []
    s, f = head, head
    while f and f.next:
        stack.append(s.val)
        f = f.next.next
        s = s.next
    if f:
        # use fast pointer to decide if the linked list has odd or even number of nodes
        # if f is None -> even
        # if f is not None -> odd
        # think like there is only one node -> f is not None

        # note: s is always in length/2 position
        s = s.next
    while s:
        if s.val != stack.pop():
            return False
        s = s.next
    return True

# time: O(n)
# space: O(n/2)

print "iterate"
l1 = Linkedlist([1,2,1])
assert iterative(l1.head)
l1 = Linkedlist([1,2,2])
assert not iterative(l1.head)


def recursive(head):
    _, res = dfs_helper(head, head)
    return res

def dfs_helper(head, origin):
    # start comparing
    if not head:
        return origin, True
    node, res = dfs_helper(head.next, origin)
    # already got answer
    if not node:
        return node, res
    if head.val != node.val:
        return None, False
    # finish comparing
    if node.next == head or node == head:
        return None, True
    # compare the next pair
    return node.next, True

# time: O(n)
# space: O(n)

print "recurisive"
l1 = Linkedlist([1,2,2,1])
assert recursive(l1.head)
l1 = Linkedlist([1,2,2])
assert not recursive(l1.head)