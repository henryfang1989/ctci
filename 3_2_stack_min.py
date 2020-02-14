# question: how could you design a stack which, in addition to push and pop,
# has a function min which returns the minimum element? Push, pop and min should
# all operate in O(1) time.

def stack_min:

    def __init__(self):
        self.s = []
