import random, copy


def choose_random_key(G):
    v1 = random.choice(list(G.keys()))
    v2 = random.choice(list(G[v1]))
    return v1, v2

def karger(G):
    length = []
    while len(G) > 2:
        v1, v2 = choose_random_key(G)
        # print(v1, v2)
        G[v1].extend(G[v2])
        # print(G[v1], G[v2])
        for x in G[v2]:
            G[x].remove(v2)
            G[x].append(v1)
        # print(G[v1], G[v2])
        while v1 in G[v1]:
            G[v1].remove(v1)
        del G[v2]
        # print(G[v1])
    for key in G.keys():
        length.append(len(G[key]))
    # print(G.keys())
    return length[0]

def operation(n,G):
    i = 0
    count = 10000
    g = {}
    while i < n:
        g = copy.deepcopy(G)
        min_cut = karger(g)
        if min_cut < count:
            count = min_cut
        i = i + 1
    print(g)
    return count


def main():
    G ={}
    with open("dd") as file:
        for line in file:
            lst = [int(s) for s in line.split()]
            G[lst[0]] = lst[1:]
    print(operation(100,G))


if __name__ == '__main__':
    main()
