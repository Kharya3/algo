import sys
from collections import defaultdict


def minfind(X, g):
    mn = sys.maxsize
    w_ = None
    v_ = None

    for v in X:
        for w, c in g[v]:
            if w not in X:
                if c < mn:
                    mn = c
                    w_ = w
                    v_ = v
    return v_, w_, mn


def main():
    g = defaultdict(list)
    with open("edges.txt") as file:
        f = file.readlines()
        n, m = map(int, f[0].split())
        for i in range(1, m + 1):
            v1, v2, c = map(int, f[i].split())
            g[v1].append((v2, c))
            g[v2].append((v1, c))
    X = {1}
    T = []
    while X != set(g.keys()):
        v, w, c = minfind(X, g)
        X.add(w)
        T.append((v, w, c))
    print(sum(i[2] for i in T))
    print(T)


if __name__ == "__main__":
    main()
