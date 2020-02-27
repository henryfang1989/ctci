# question: Given a directed graph, design an algorithm to find out whether
# there is a route between two needs.

from collections import deque
from utils import Graph

def bfs(start, end):
    if start == end:
        return True
    visited = set()
    q = deque()
    q.append(start)
    visited.add(start)
    while q:
        node = q.popleft()
        for child in node.children:
            if child == end:
                return True
            if child not in visited:
                q.append(child)
                visited.add(child)
    return False
# time: O(n)
# space: O(n)

def dfs(start, end):
    return dfs_helper(start, end, set())

def dfs_helper(start, end, visited):
    visited.add(start)
    if start == end:
        return True
    for child in start.children:
        if child not in visited and dfs(child, end):
            return True
    visited.remove(start)
    return False
# time: O(n)
# space: O(n)

g = Graph()
g.connect(1, [2,3,4])
g.connect(2, [2,5])
g.connect(3, [6,5])
g.connect(7, [8])
assert bfs(g.get_node(1), g.get_node(5))
assert not bfs(g.get_node(1), g.get_node(8))
assert dfs(g.get_node(1), g.get_node(5))
assert not dfs(g.get_node(1), g.get_node(8))