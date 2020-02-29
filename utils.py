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


class GraphNode:
	def __init__(self, name):
		self.name = name
		self.children = []

	# connect node with other nodes
	def connect(self, children):
		if isinstance(children, list):
			self.children += children
		else:
			self.children.append(children)

	def __repr__(self):
		msg = "{}->".format(self.name)
		msg += "[" +  ",".join([str(child.name) for child in self.children]) + "]"
		return msg

class Graph:
	def __init__(self):
		self.nodes = {}

	# guarantee the node exists in graph. create a new node if
	# it does not exist
	def ensure_node(self, name):
		if name not in self.nodes:
			self.nodes[name] = GraphNode(name)
		return self.nodes[name]

	# connect current node with other nodes
	def connect(self, name, children_names):
		root = self.ensure_node(name)
		if isinstance(children_names, list):
			for child_name in children_names:
				root.connect(self.ensure_node(child_name))
		else:
			root.connect(self.ensure_node(children_names))

	def get_node(self, name):
		return self.nodes.get(name, None)

	def __repr__(self):
		return "{}".format(self.nodes)

class BinaryTreeNode:
	def __init__(self, name):
		self.name = name
		self.left = None
		self.right = None

	def __repr__(self):
		msg = str(self.name) + "->"
		msg += str(self.left.name) if self.left else "[]"
		msg += ","
		msg += str(self.right.name) if self.right else "[]"
		return msg

from collections import deque
def binary_tree_print(root):
	q = deque()
	q.append(root)
	while q:
		sz = len(q)
		row = []
		for _ in xrange(sz):
			node = q.popleft()
			if node:
				row.append(str(node.name))
			else:
				row.append("[]")
			if not node or (not node.left and not node.right):
				continue
			q.append(node.left)
			q.append(node.right)
		print " ".join(row)

import random
def build_random_tree_from_array(array, nodes=None):
	if not array:
		return None
	s = random.randint(0, len(array)-1)
	root = BinaryTreeNode(array[s])
	if nodes is not None:
		nodes[array[s]] = root
	root.left =build_random_tree_from_array(array[:s], nodes)
	root.right =build_random_tree_from_array(array[s+1:], nodes)
	return root

class BinaryTreeNodeWithParent:
	def __init__(self, name):
		self.name = name
		self.left = None
		self.right = None
		self.parent = None

	def __repr__(self):
		msg = str(self.name) + "->"
		msg += str(self.left.name) if self.left else "[]"
		msg += ","
		msg += str(self.right.name) if self.right else "[]"
		msg += ","
		msg += str(self.parent.name) if self.parent else "[]"
		return msg

def build_random_tree_with_parent_from_array(array, nodes=None):

	def helper(array, parent, nodes):
		if not array:
			return None
        s = random.randint(0, len(array)-1)
        root = BinaryTreeNodeWithParent(array[s])
        nodes[array[s]] = root
        root.parent = parent
        root.left =helper(array[:s], root, nodes)
        root.right =helper(array[s+1:], root, nodes)
        return root

	return helper(array, None, nodes)