from collections import defaultdict
from time import time


class Graph:
    start = time()

    def __init__(self):
        self.graph = defaultdict(list)
        self.num_nodes = 875715
        self.ln_scc = []

    def SCC(self):
        explored = [False] * self.num_nodes
        stack = []
        t1 = time()
        print("Taken input in ", t1 - self.start)
        for i in range(1, self.num_nodes):
            if i not in explored:
                print(i)
                explored[i] = True
                temp_stack = [i]
                while temp_stack:
                    curr = temp_stack[-1]
                    unx_child = False
                    for j in range(1, self.num_nodes):
                        if curr in self.graph[j] and not explored[j]:
                            unx_child = True
                            explored[j] = True
                            temp_stack.append(j)
                    if not unx_child:
                        c = temp_stack.pop()
                        if c not in stack:
                            stack.insert(0, c)
        t2 = time()
        print("First call comp in ", t2 - t1)

        explored = [False] * self.num_nodes

        while stack:
            s = stack.pop(0)
            if not explored[s]:
                print(s)
                st = []
                explored[s] = True
                temp_stack = [s]
                while temp_stack:
                    curr = temp_stack[-1]
                    unx_child = False
                    for j in self.graph[curr]:
                        if not explored[j]:
                            explored[j] = True
                            unx_child = True
                            temp_stack.append(j)
                    if not unx_child:
                        st.insert(0, temp_stack.pop())
                self.ln_scc.append(len(st))
        end = time()
        print("Second call complete in ", end - t2)
        print(" Total time ", end - self.start)


print("Running")
gr = Graph()
with open("SCC.txt") as file:
    for line in file:
        if line != "\n":
            items = line.split()
            gr.graph[int(items[0])] += [int(items[1])]
print("Taken Input")
gr.SCC()
