# question: how could you design a stack which, in addition to push and pop,
# has a function min which returns the minimum element? Push, pop and min should
# all operate in O(1) time.

# Sol #1, just work as normal stack, but search for minimum val when call min()
class stack_min_search:
    def __init__(self):
        self.s = []

    def push(self, val):
        self.s.append(val)

    def pop(self):
        if not self.s:
            raise Exception("stack is empty")
        return self.s.pop()

    # time: O(n)
    # space: O(1)
    def min(self):
        if not self.s:
            raise Exception("stack is empty")
        return min(self.s)


s = stack_min_search()
s.push(4)
s.push(5)
assert s.min() == 4
s.push(2)
s.push(1)
s.pop()
assert s.min() == 2

# Sol #2 use a second stack to always record the minimum val in current stack
class stack_min_stack:

    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val):
        if not self.m or self.m[-1] >= val:
            self.m.append(val)
        self.s.append(val)

    def pop(self):
        if not self.s:
            raise Exception("stack is empty")
        ret = self.s.pop()
        if self.m[-1] >= ret:
            self.m.pop()
        return ret

    # time: O(1)
    # space: O(n)
    def min(self):
        if not self.m:
            raise Exception("stack is empty")
        return self.m[-1]

s = stack_min_stack()
s.push(4)
s.push(5)
assert s.min() == 4
s.push(2)
assert s.min() == 2
s.push(1)
assert s.min() == 1
s.pop()
assert s.min() == 2


class stack_min_diff:

    def __init__(self):
        self.s = []
        self.m = 0

    def push(self, val):
        if not self.s or val < self.m:
            self.s.append(val-self.m)
            self.m = val
        else:
            self.s.append(val-self.m)

    def pop(self):
        if not self.s:
            raise Exception("stack is empty")
        ret = self.s.pop()
        if ret > 0:
            ret += self.m
        else:
            ret, self.m = self.m, self.m - ret
        return ret

    def min(self):
        return self.m

s = stack_min_diff()
s.push(4)
s.push(5)
assert s.min() == 4
s.push(2)
assert s.min() == 2
s.push(1)
assert s.min() == 1
s.pop()
assert s.min() == 2

