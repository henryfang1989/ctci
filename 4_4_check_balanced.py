# question: Implement a function to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined to be a
# tree  such that the heights of the two subtrees of any node never differ
# by more than one

def check_balanced(root):
    res, _ = dfs_helper(root)
    return res

# divide and conquer
# time: O(n)
# space O(logn) tree depth
def dfs_helper(root):
    if not root:
        return True, 0
    lb, lh = dfs_helper(root.left)
    rb, rh = dfs_helper(root.right)
    if not lb or not rb or lh > rh+1 or rh > lh+1:
        return False, 0
    return True, max(lh, rh) + 1

from utils import build_random_tree_from_array, binary_tree_print

root = build_random_tree_from_array([1,2,3,4])
binary_tree_print(root)
print check_balanced(root)