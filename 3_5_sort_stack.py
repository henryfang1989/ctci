# question: Write a program to sort a stack such that the smallest items are on
# the top. You can use an additional temporary stack, but you may not copy the
# elements into any other data structure (such as an array). The stack supports
# the following operations: push, pop, peek and isEmpty.

from utils import Stack

def sort_stack(stack):
    buf = Stack()
    while not stack.is_empty():
        cur = stack.pop()
        cnt = 0
        while not buf.is_empty() and cur < buf.peek():
            stack.push(buf.pop())
            cnt += 1
        buf.push(cur)
        for i in xrange(cnt):
            buf.push(stack.pop())
    while not buf.is_empty():
        stack.push(buf.pop())
        
# time: O(n^2)
# space: O(n)

s = Stack()
s.push(1)
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.print_stack()
sort_stack(s)
s.print_stack()
            
