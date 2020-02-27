# question: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binay search tree with minimal height

from utils import BinaryTreeNode, binary_tree_print

def build_tree_dfs(array):
    if not array:
        return None
    mid = len(array) / 2
    root = BinaryTreeNode(array[mid])
    root.left = build_tree_dfs(array[:mid])
    root.right = build_tree_dfs(array[mid+1:])
    return root

root = build_tree_dfs([1,2,3,4,5,6])
