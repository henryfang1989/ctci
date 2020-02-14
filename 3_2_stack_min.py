# question: how could you design a stack which, in addition to push and pop,
# has a function min which returns the minimum element? Push, pop and min should
# all operate in O(1) time.

# Sol #1, just work as normal stack, but search for minimum val when call min()
class stack_min:
    def __init__(self):
        self.s = []

    def push(self, val):
        self.s.append(val)

    def pop(self):
        if not self.s:
            raise Exception("stack is empty")
        return self.s.pop()

    def min(self):
        if not self.s:
            raise Exception("stack is empty")
        return min(self.s)


s = stack_min()
s.push(4)
s.push(5)
assert s.min() == 4
s.push(2)
s.push(1)
s.pop()
assert s.min() == 2