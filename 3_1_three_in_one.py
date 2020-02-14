# question: describle how you could use a single array to implement three stacks.

# Sol #1: split the array in even ranges for each stack
class ThreeInOne:
    def __init__(self, N):
        self.array = [None] * N
        self.indexs = [0, N/3, N/3*2]
        self.ranges = [(0, N/3), (N/3, N/3*2), (N/3*2, N)]

    def push(self, stack_num, val):
        index = self.indexs[stack_num]
        range = self.ranges[stack_num]
        if index >= range[1]:
            raise Exception("stack {} is full".format(stack_num))
        self.array[index] = val
        self.indexs[stack_num] += 1

    def pop(self, stack_num):
        index = self.indexs[stack_num]
        range = self.ranges[stack_num]
        if index <= range[0]:
            raise Exception("stack {} is empty".format(stack_num))
        # the index always points to the next available empty pos
        ret = self.array[index-1]
        self.array[index-1] = None
        self.indexs[stack_num] -= 1
        return ret

    def peek(self, stack_num):
        index = self.indexs[stack_num]
        range = self.ranges[stack_num]
        if index <= range[0]:
            raise Exception("stack {} is empty".format(stack_num))
        # the index always points to the next available empty pos
        return self.array[index-1]

    def isEmpty(self, stack_num):
        index = self.indexs[stack_num]
        return index <= self.ranges[stack_num][0]

    def print_stack(self):
        for i in xrange(3):
            start, end = self.ranges[i][0], self.indexs[i]
            print(",".join([str(self.array[k]) for k in xrange(start, end)]))


# Sol #2: set dynamic bounds for each stack.
class single_stack:
    def __init__(self, start, capacity, array, id):
        self.id = id
        self.start = start
        self.capacity = capacity
        self.array = array
        self.size = 0

    def index(self, i):
        return i % len(self.array)

    def next_index(self, i):
        return (i+1) % len(self.array)

    def push(self, val):
        self.array[self.index(self.start + self.size)] = val
        self.size += 1
        self.capacity = max(self.capacity, self.size)

    def pop(self):
        if self.size == 0:
            raise Exception("stack is empty")
        ret = self.array[self.index(self.start + self.size - 1)]
        self.array[self.index(self.start + self.size - 1)] = None
        self.size -= 1
        return ret

    def peek(self):
        if self.size == 0:
            raise Exception("stack is empty")
        return self.array[self.index(self.start + self.size -1)]

    def isEmpty(self):
        return self.size == 0

    def shift(self):
        if self.size >= self.capacity:
            self.capacity += 1
        for i in xrange(self.size, 0, -1):
            index1, index2 = self.index(self.start + i), self.index(self.start + i - 1)
            self.array[index1] = self.array[index2]
            print "stack {}, move {}:{} to {}:{}".format(self.id, index2, self.array[index2], index1, self.array[index1])
        self.array[self.index(self.start)] = None
        self.start += 1
        self.capacity -= 1

    def isFull(self):
        return self.size >= self.capacity

    def print_stack(self):
        msg = ",".join([str(self.array[self.index(self.start+i)]) for i in xrange(self.size)])
        print(msg)


class ThreeInOne_Dynamic:
    def __init__(self, num_of_stacks, stack_size):
        self.num_of_stacks = num_of_stacks
        self.array = [None] * num_of_stacks * stack_size
        self.stacks = [single_stack(i*stack_size, stack_size, self.array, i) for i in xrange(num_of_stacks)]

    def shift_helper(self, stack_num, origin_stack_num):
        stack_num, origin_stack_num = stack_num % self.num_of_stacks, origin_stack_num % self.num_of_stacks
        print "try to shift stack {}".format(stack_num)
    	if stack_num == origin_stack_num:
    		return False
        s = self.stacks[stack_num]
        if s.isFull() and not self.shift_helper(stack_num+1, origin_stack_num):
        	return False
        s.shift()
        return True

    # time: O(n)
    # space: O(m)
    # n = total elements in stack, m = # of single stacks
    def shift(self, stack_num):
        stack_num %= self.num_of_stacks
        if not self.shift_helper(stack_num, stack_num-1):
            raise Exception("No space left in multi-stack")

    def push(self, stack_num, val):
        s = self.stacks[stack_num]
        if s.isFull():
            self.shift(stack_num+1)
        s.push(val)

    def pop(self, stack_num):
        s = self.stacks[stack_num]
        return s.pop()

    def peek(self, stack_num):
        return self.stacks[stack_num].peek()

    def isEmpty(self, stack_num):
        return self.stacks[stack_num].isEmpty()

    def print_stack(self):
        for s in self.stacks:
            s.print_stack()


stack = ThreeInOne_Dynamic(3,4)
stack.push(0,1)
stack.push(0,2)
stack.push(0,2)
stack.push(0,2)
stack.push(0,2)
stack.push(2,3)
stack.push(2,5)
stack.push(1,3)
stack.push(1,4)
stack.push(1,4)
stack.push(1,4)
stack.push(1,4)
stack.pop(0)
stack.pop(0)
stack.print_stack()
stack.push(1,4)
stack.push(1,4)
stack.pop(0)
stack.pop(0)
stack.pop(0)
stack.push(1,4)
stack.push(1,4)
stack.push(1,4)
stack.pop(2)
stack.pop(2)
stack.push(1,4)
stack.push(1,4)
stack.pop(1)
stack.pop(1)
stack.push(2, 1)
stack.push(2, 1)
stack.pop(2)
stack.push(0,2)
stack.print_stack()
