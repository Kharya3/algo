from collections import defaultdict


class graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[-1*u].append(v)
        self.graph[-1*v].append(u)

    def vertices(self):
        return list(self.graph.keys())


def kosaraju():
    explored = [False] * 2*num_nodes
    stack = []
    for i in gr.vertices():
        if i not in explored:
            explored[i] = True
            temp_stack = [i]
            while temp_stack:
                curr = temp_stack[-1]
                unx_child = False
                for j in gr.vertices():
                    if curr in gr.graph[j] and not explored[j]:
                        unx_child = True
                        explored[j] = True
                        temp_stack.append(j)
                if not unx_child:
                    c = temp_stack.pop()
                    if c not in stack:
                        stack.insert(0, c)

    explored = [False] * 2*num_nodes
    print(stack)
    while stack:
        s = stack.pop(0)
        # print(s)
        if not explored[s]:
            st = []
            explored[s] = True
            temp_stack = [s]
            while temp_stack:
                curr = temp_stack[-1]
                unx_child = False
                for j in gr.graph[curr]:
                    if not explored[j]:
                        explored[j] = True
                        unx_child = True
                        temp_stack.append(j)
                if not unx_child:
                    st.insert(0, temp_stack.pop())
            scc.append(st)


def take_input():
    for i in range(m):
        x, y = map(int, input().split())
        gr.add_edge(x, y)


if __name__ == "__main__":
    num_nodes, m = map(int, input().split())
    gr = graph()
    take_input()
    print(gr.graph)
    scc = []
    kosaraju()
    print(scc)
    for lst in scc:
        for i in lst:
            if (-1*i) in lst:
                print("Not solvable")
                break
        else:
            continue
        break
    else:
        print("Solvable")
