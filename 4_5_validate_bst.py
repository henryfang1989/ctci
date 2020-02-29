# question: Implement a function to check if a binary tree is
# a binary search tree

def validate1(root):
    res, _, _ = divide_conquer(root)
    return res

def validate2(root):
    return in_order_traverse_compare(root)

def validate(root):
    return dfs_traverse(root, float('-inf'), float('inf'))

def divide_conquer(root):
    if not root:
        return True, float('-inf'), float('inf')
    # divide and conquer
    lv, lmin, lmax = divide_conquer(root.left)
    rv, rmin, rmax = divide_conquer(root.right)
    if not lv or not rv:
        return False, 0, 0
    if lmax == float('inf') and rmin == float('-inf'):
        return True, root.name, root.name
    if lmax == float('inf') and root.name < rmin:
        return True, root.name , rmax
    if rmin == float('-inf') and root.name >= lmax:
        return True, lmin, root.name
    if lmax <= root.name < rmin:
        return True, lmin, rmax
    return False, 0, 0
# time: O(n)
# space: O(logn)

current = None
def in_order_traverse_compare(root):
    global current
    if not root:
        return True
    l = in_order_traverse_compare(root.left)
    if not l:
        return False
    # it does not allow left <= root
    if current is not None and root.name <= current:
        return False
    current = root.name
    r = in_order_traverse_compare(root.right)
    if not r:
        return False
    return True
# time: O(n)
# space: O(logn)

def dfs_traverse(root, left, right):
    if not root:
        return True
    if not left <= root.name < right:
        return False
    if not dfs_traverse(root.left, left, root.name) or not dfs_traverse(root.right, root.name, right):
        return False
    return True
# time: O(n)
# space: O(logn)

from utils import build_random_tree_from_array, binary_tree_print

root = build_random_tree_from_array([])
binary_tree_print(root)
assert validate(root)
root = build_random_tree_from_array([-1,2,3,4,5,6])
binary_tree_print(root)
assert validate(root)
root = build_random_tree_from_array([3,3,3,3])
binary_tree_print(root)
# left <= root < right => binary search tree
assert not validate(root)
root = build_random_tree_from_array([3,3,-3,3])
binary_tree_print(root)
assert not validate(root)