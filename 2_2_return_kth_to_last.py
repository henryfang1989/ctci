# question: implement an alogrithm to find the kth to last element of singly linked list.

from linked_list import Linkedlist

def kth_to_last(head, k):
    fast = slow = head
    while k > 0 and fast:
        fast = fast.next
        k -= 1
    
    # link list is shorter than k
    if k > 0 and not fast:
        return None

    while fast:
        fast = fast.next
        slow = slow.next

    return slow.val

# time: O(n)
# space: O(1)

ll = Linkedlist([1,2,3,4,5])
print kth_to_last(ll.head, 3)
print kth_to_last(ll.head, 2)
