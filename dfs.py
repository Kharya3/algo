from collections import deque, defaultdict


def dfs_topo(i, stack):
    explored.append(i)
    for edge in graph[i]:
        if edge not in explored:
            dfs_topo(edge, stack)
    stack.insert(0, i)


def Toposrt():
    stack = []
    for i in range(1, len(graph) + 1):
        if i not in explored:
            dfs_topo(i, stack)
    return stack


def dfs(vertex):
    stack = deque(vertex)
    while stack:
        ver = stack.pop()
        if ver not in explored:
            explored.append(ver)
            for edge in graph[ver]:
                stack.append(edge)


num_nodes = int(input())
graph = defaultdict(list)
explored = []
explored1 = []
ln_scc = []
with open("graph.txt") as file:
    for line in file:
        if line != "\n":
            items = line.split()
            graph[int(items[0])] += [int(items[1])]
print(Toposrt())
