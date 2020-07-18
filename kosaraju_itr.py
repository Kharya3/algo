from collections import defaultdict


def main():
    with open("SCC.txt") as file:
        for line in file:
            if line != "\n":
                items = line.split()
                gr[int(items[0])] += [int(items[1])]

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

    explored = [False] * num_nodes

    while stack:
        s = stack.pop(0)
        print(s)
        if not explored[s]:
            st = []
            explored[s] = True
            temp_stack = [s]
            while temp_stack:
                curr = temp_stack[-1]
                unx_child = False
                for j in gr[curr]:
                    if not explored[j]:
                        explored[j] = True
                        unx_child = True
                        temp_stack.append(j)
                if not unx_child:
                    st.insert(0, temp_stack.pop())
            ln_scc.append(len(st))


if __name__ == "__main__":
    num_nodes = 875715
    gr = defaultdict(list)
    ln_scc = []
    main()
    print(sorted(ln_scc, reverse=True)[:5])