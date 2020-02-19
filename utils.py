class Node:

	def __init__(self, val):
		self.val = val
		self.next = None

class Linkedlist:

	def __init__(self, array):
		self.head = None
		self.tail = None
		self.list_to_ll(array)

	def list_to_ll(self, array):
		for num in array:
			self.append(num)

	def append(self, val):
		new_node = Node(val)
		if not self.head:
			self.head = new_node
		else:
			self.tail.next = new_node
		self.tail = new_node

	def __repr__(self):
		tmp = self.head
		msg = ""
		while tmp:
			if tmp.next:
				msg += str(tmp.val) + ' -> '
			else:
				msg += str(tmp.val)
			tmp = tmp.next
		return msg

def print_linkedlist(head):
	tmp = head
	msg = ""
	while tmp:
		if tmp.next:
			msg += str(tmp.val) + ' -> '
		else:
			msg += str(tmp.val)
		tmp = tmp.next
	print msg

class Stack:
	def __init__(self):
		self.s = []

	def push(self, val):
		self.s.append(val)

	def pop(self):
		if not self.s:
			raise Exception("stack is empty")
		return self.s.pop()

	def size(self):
		return len(self.s)

	def is_empty(self):
		return not self.s

	def peek(self):
		if not self.s:
			raise Exception("stack is empty")
		return self.s[-1]

	def __repr__(self):
		return " ".join([str(e) for e in self.s])

from collections import deque
class Queue:
	def __init__(self):
		self.q = deque()

	def enqueue(self, val):
		self.q.append(val)

	def dequeue(self):
		self.check_empty()
		return self.q.popleft()

	def peek(self):
		self.check_empty()
		return self.q[0]

	def check_empty(self):
		if not self.q:
			raise Exception("Queue is empty")

	def is_empty(self):
		return not self.q

	def __repr__(self):
		return " ".join([str(e) for e in self.q])