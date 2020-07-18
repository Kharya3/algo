from Union_find import UnionFind as uf


def Kruskal(edges, vertices):
    T = []
    U = uf(arr=vertices)
    # print(U.arr,U.parent,U.size,U.n_comp)
    edges.sort(key=lambda x: x[2])
    # print(edges)
    for v, w, c in edges:
        if U.find(v) != U.find(w):
            T.append([v, w])
            U.union(v, w)
            # print(v, w, c,U.parent,U.size,U.n_comp)
    z = 1
    print(U.size.index(max(U.size)))
    return T


def takeInp():
    edges = []
    # vertices = []
    with open("edges.txt") as file:
        f = file.readlines()
        n, m = map(int, f[0].split())
        for i in range(1, m + 1):
            v1, v2, c = map(int, f[i].split())
            edges.append([v1, v2, c])
    vertices= [i+1 for i in range(n)]
    return edges, vertices


def main():
    edges, vertices = takeInp()
    print(edges)
    k = Kruskal(edges, vertices)
    print(k)


if __name__ == "__main__":
    main()
