# question: Implement a MyQueue class which implements a queue using two stacks
from utils import Stack

class MyQueue:
    def __init__(self):
        self.front = Stack()
        self.end = Stack()

    def size(self):
        return self.front.size() + self.end.size()

    def enqueue(self, val):
        self.end.push(val)

    def dequeue(self):
        if self.front.is_empty() and not self.move():
            raise Exception("queue is empty")
        return self.front.pop()

    def peek(self):
        if self.front.is_empty() and not self.move():
            raise Exception("queue is empty")
        return self.front.peek()

    # time: O(n), however, the average is O(1)
    def move(self):
        moved = False
        while not self.end.is_empty():
            moved = True
            self.front.push(self.end.pop())
        return moved

    def print_q(self):
        print self.front
        print self.end

q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.print_q()
print(q.dequeue())
q.print_q()
q.enqueue(5)
q.enqueue(6)
q.print_q()
q.dequeue()
q.print_q()
print(q.peek())