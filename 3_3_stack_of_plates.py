# question: Imagine a (literal) stack of plates. If the stack gets too high, it maight topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds
# some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should complsed of
# of several stacks and should create a new stack once the previous one exceeds capacity
# SetOfStacks.push() and SetofStacks.pop() should behave identically to a single stack (that
# is, pop() should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific substack.

class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, val):
        if not self.stacks or len(self.stacks[-1]) >= self.capacity:
            self.stacks.append([val])
        else:
            self.stacks[-1].append(val)

    def pop(self):
        if not self.stacks:
            raise Exception("stack is empty")
        ret = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return ret

    def isEmpty(self):
        return not self.stacks

    def peek(self):
        if not self.stacks:
            raise Exception("stack is empty")
        return self.stacks[-1][-1]

    def popAt(self, index):
        if index < len(self.stacks):
            stack = self.stacks[index]
            ret = stack.pop()
            if not stack:
                del self.stacks[index]
            return ret
        raise Exception("stack is empty")

    def print_stacks(self):
        print "stack print begin"
        for i, s in enumerate(self.stacks):
            print "stack {}: {}".format(i, s)
        print "stack print end"

s = SetOfStacks(2)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.print_stacks()
s.pop()
s.popAt(1)
s.popAt(1)
s.popAt(1)
s.pop()
s.print_stacks()