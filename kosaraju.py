import time
from collections import defaultdict


def dfs_topo_rev(s, stack, explored):
    explored[s] = True
    for i in range(1, num_nodes):
        if s in gr[i] and not explored[i]:
            dfs_topo_rev(i, stack, explored)
    stack.insert(0, s)


def Toposrt(explored):
    stack = []
    for i in range(1, num_nodes):
        if not explored[i]:
            # print(i)
            dfs_topo_rev(i, stack, explored)
    return stack


def dfs_topo(s, _scc, explored):
    explored[s] = True
    _scc.append(s)
    # print(s, end=" ")
    for edge in gr[s]:
        if not explored[edge]:
            dfs_topo(edge, _scc, explored)
    return _scc


def main():
    # start = time.time()
    # print("Running...")
    with open("graph.txt") as file:
        for line in file:
            if line != "\n":
                items = line.split()
                gr[int(items[0])] += [int(items[1])]

    # print(gr)
    # mid = time.time()
    # print("Taken Input...\nin ", mid - start)
    explored = [False] * num_nodes
    stack = Toposrt(explored)
    mid1 = time.time()
    # print("first Dfs complete...\nin ", mid1 - mid)
    explored = [False] * num_nodes
    while stack:
        i = stack.pop(0)
        count = 1
        _scc = []
        if not explored[i]:
            _scc = dfs_topo(i, _scc, explored)
            # print("")
            # print(_scc)
            ln_scc.append(len(_scc))
    print(sorted(ln_scc, reverse=True)[:5])
    # end = time.time()
    # print("completed...\nin ", end - mid1)


if __name__ == "__main__":
    num_nodes = 9
    gr = defaultdict(list)
    ln_scc = []
    main()
