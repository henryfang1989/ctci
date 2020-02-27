# question: Give a binary tree, design an algorithm which creates a linked list of all the
# nodes at each depth (e.g. if you have a tree with depth D, you'll have D linked list)

from utils import Linkedlist, BinaryTreeNode, build_random_tree_from_array, binary_tree_print

def create_dfs(root):
    res = []
    dfs_helper(root, 0, res)
    return res

def create_bfs(root):
    return bfs_helper(root)

def dfs_helper(root, level, res):
    if not root:
        return
    if len(res) == level:
        res.append(Linkedlist([root.name]))
    else:
        res[level].append(root.name)
    dfs_helper(root.left, level+1, res)
    dfs_helper(root.right, level+1, res)

from collections import deque
def bfs_helper(root):
    res = []
    q = deque()
    q.append(root)
    while q:
        cur = Linkedlist([])
        sz = len(q)
        for _ in xrange(sz):
            node = q.popleft()
            cur.append(node.name)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(cur)
    return res

root = build_random_tree_from_array([1,2,3,4,5,6, 7, 8, 9])
binary_tree_print(root)
lls = create_dfs(root)
print lls

root = build_random_tree_from_array([1,2,3,4,5,6, 7, 8, 9])
binary_tree_print(root)
lls = create_bfs(root)
print lls