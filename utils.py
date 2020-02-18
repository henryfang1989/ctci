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

	def print_ll(self):
		tmp = self.head
		msg = ""
		while tmp:
			if tmp.next:
				msg += str(tmp.val) + ' -> '
			else:
				msg += str(tmp.val)
			tmp = tmp.next
		print msg

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

	def print_stack(self):
		print self.s