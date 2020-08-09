from random import choice


def graph():
    g = {}
    with open("kargerMinCut.txt") as file:
        for line in file:
            lst = [int(i) for i in line.split()]
            g[lst[0]] = lst[1:]
    return g


def karger(g):
    m = 10000
    while len(g) > 2:
        v = choice(list(g.keys()))
        w = choice(g[v])
        for ver in g[w]:
            if ver != v:
                g[v].append(ver)
            g[ver].remove(w)
            if ver != v:
                g[ver].append(v)
        del g[w]
        n = len(g[list(g.keys())[0]])
        if n < m:
            m = n
    return m


def main():
    n = 10
    o = 100
    for i in range(n):
        m = karger(graph())
        if m < o:
            o = m
    print(o)


if __name__ == '__main__':
    main()
