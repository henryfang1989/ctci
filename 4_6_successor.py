# question: Write an algorithm to find the "next" node
# (i.e., in-order successor) of a given node in binary search
# tree. You may assume that each node has a link to its parent.

def successor(node):
    # if find right subtree -> return leftmost node of right subtree
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    else:
        # if cannot find right subtree -> need to find a parent, whose
        # left subtree includes the node
        c = node
        p = node.parent
        while p and p.left != c:
            c = p
            p = c.parent
        return p

# time: O(logn)
# space: O(1)
# n is total # of nodes in tree

from utils import build_random_tree_with_parent_from_array, binary_tree_print

nodes = {}
root =build_random_tree_with_parent_from_array([1,2,3,4,5,6,7,8,9], nodes)
binary_tree_print(root)
assert successor(nodes[5]).name == 6
assert successor(nodes[2]).name == 3
assert successor(nodes[9]) == None