import random,copy


def kargerMinCut(graph,m):
    while len(graph) > 2:
         v = random.choice(list(graph.keys()))
         w = random.choice(graph[v])
         contract(graph, v, w)
    mincut = len(graph[list(graph.keys())[0]])
    l = []
    if mincut<m:
        m = mincut
        l = list(graph.keys())
    return m,l


def contract(graph, v, w):
    for node in graph[w]:  # merge the nodes from w to v
         if node != v:  # we dont want to add self-loops
             graph[v].append(node)
         graph[node].remove(w)  # delete the edges to the absorbed
         if node != v:
              graph[node].append(v)
    del graph[w]  # delete the absorbed vertex 'w'


G ={}; n= 100
with open("dd") as file:
    for line in file:
        lst = [int(s) for s in line.split()]
        G[lst[0]] = lst[1:]
m = 10000
l = []
for i in range(n):
    m, l=kargerMinCut(copy.deepcopy(G),m)
print(m, l)
