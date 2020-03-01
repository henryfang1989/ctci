# question: You are given a list of projects and
# list of dependencies (which is a lost of pairs
# of projects, where the second projects dependent
# on the first prject). All of a project's  dependencies
# must be built before the project is. Find a build
# order that will allow the projects to be built.
# If there is no valid build order, return an error.


# topological sort
# build a project graph and count each projects'
# dependencies and next projects.
# BFS to iterate all pojects without dependencies
# and record the order of iteration.
def build(projects):
    # build the graph of projects
    nexts = {}
    deps_cnt = {}
    # O(e)
    for prev, cur in projects:
        if prev not in nexts:
            nexts[prev] = []
        nexts[prev].append(cur)
        if cur not in nexts:
            nexts[cur] = []

        if prev not in deps_cnt:
            deps_cnt[prev] = 0
        if cur not in deps_cnt:
            deps_cnt[cur] = 0
        deps_cnt[cur] += 1

    from collections import deque
    q = deque()
    # O(n)
    for k, v in deps_cnt.items():
        if v == 0:
            q.append(k)

    res = []
    # O(e)
    while q:
        node = q.popleft()
        res.append(node)
        for p in nexts[node]:
            deps_cnt[p] -= 1
            if deps_cnt[p] == 0:
                q.append(p)
    if len(res) != len(nexts):
        return "ERROR"
    return res


# time: O(n+e)
# space: O(n)
# n is total number of projects, e is total number of dependencies

projects = [(1, 2), (2, 3), (1, 3), (4, 5)]
print build(projects)
projects = [(1, 2), (2, 3), (3, 2), (4, 5)]
print build(projects)

# DFS
# 1. build the graph (dep -> next)
# 2. use DFS to set the order of all children of a dep node and add
# the dep node to the begining of build order


def dfs_build(projects):
    # build graph
    graph = {}
    states = {}  # 0:unvisited, 1:processing, 2:finished
    # O(e)
    for prev, cur in projects:
        if prev not in graph:
            graph[prev] = []
        if cur not in graph:
            graph[cur] = []
        graph[prev].append(cur)
        states[prev] = 0
        states[cur] = 0

    # dfs set the build order
    from collections import deque
    order = deque()
    for p in graph:
        if not dfs_helper(p, graph, states, order):
            return "ERROR"
    return list(order)


# memorization DFS
def dfs_helper(project, graph, states, build_order):
    if states[project] == 1:
        return False
    if states[project] == 2:
        return True
    if not graph[project]:
        states[project] = 2
        build_order.appendleft(project)
        return True
    states[project] = 1
    for p in graph[project]:
        if not dfs_helper(p, graph, states, build_order):
            return False
    states[project] = 2
    build_order.appendleft(project)
    return True


# time: O(n+e)
# space: O(n)

projects = [(1, 2), (2, 3), (1, 3), (4, 5)]
print dfs_build(projects)
projects = [(1, 2), (2, 3), (3, 2), (4, 5)]
print dfs_build(projects)
