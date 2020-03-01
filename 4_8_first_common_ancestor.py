# question: Design an algorithm and write code to
# find the first common ancestor of two nodes in
# a binary tree. Avoid storing additional nodes in
# a data structure. Note: this is not necessarily
# a binary search tree.

# Sol #1 with links to parents
def ancestor(node1, node2):
    if node1 == node2:
        return node1
    visited = set()
    while node1 or node2:
        if node1 in visited:
            return node1
        if node2 in visited:
            return node2
        visited.add(node1)
        visited.add(node2)
        if node1:
            node1 = node1.parent
        if node2:
            node2 = node2.parent
    return None

from utils import build_random_tree_with_parent_from_array, binary_tree_print

nodes = {}
root = build_random_tree_with_parent_from_array([3,4,7,5,6,8,1,2,9], nodes)
binary_tree_print(root)
print ancestor(nodes[5], nodes[6])

def ancestor2(node1, node2):
    