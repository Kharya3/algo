# class Gr:
#     def __init__(self):
#         self.__dttype = {}
#
#     def vertices(self):
#         return list(self.__dttype.keys())
#
#     def add_vertex(self, vertex):
#         if vertex not in self.__dttype:
#             self.__dttype[vertex] = []
#
#     def add_edge(self, edge):
#         edge = set(edge)
#         v, w = tuple(edge)
#         self.__dttype[v].append(w)
#
#     def edges(self):
#         edges = []
#         for v in self.__dttype:
#             for w in self.__dttype[v]:
#                 if {v, w} not in edges:
#                     edges.append({v, w})
#         return edges
#
#     def __str__(self):
#         res = "vertices: "
#         for k in self.__dttype:
#             res += str(k) + " "
#         res += "\nedges: "
#         for edge in self.edges():
#             res += str(edge) + " "
#         return res
#
from collections import defaultdict


def top_srt_rev():
    explored = [False] * num_nodes
    stack = []
    for i in range(1, num_nodes):
        if i not in explored:
            explored[i] = True
            temp_stack = [i]
            while temp_stack:
                curr = temp_stack[-1]
                unx_child = False
                for j in range(1, num_nodes):
                    if curr in gr[j] and not explored[j]:
                        unx_child = True
                        explored[j] = True
                        temp_stack.append(j)
                if not unx_child:
                    c = temp_stack.pop()
                    if c not in stack:
                        stack.insert(0, c)
    print(stack)


def top_srt():
    explored = []
    stack = []
    for i in range(1,num_nodes):
        if i not in explored:
            explored.append(i)
            temp_stack = [i]
            while temp_stack:
                curr = temp_stack[-1]
                unx_child = False
                for j in r_gr[curr]:
                    if j not in explored:
                        unx_child = True
                        explored.append(j)
                        temp_stack.append(j)
                if not unx_child:
                    stack.insert(0, temp_stack.pop())
    print(stack)


if __name__ == "__main__":
    num_nodes = int(input())
    gr = defaultdict(list)
    r_gr = defaultdict(list)
    with open("graph.txt") as file:
        for line in file:
            if line != "\n":
                items = line.split()
                gr[int(items[0])].append(int(items[1]))
                r_gr[int(items[1])] += [int(items[0])]
    print(gr)
    top_srt()
    top_srt_rev()





