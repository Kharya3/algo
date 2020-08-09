from collections import defaultdict


def djk(s):
    X = {s}
    ln[s] = 0
    while X:
        v = X.pop()
        for w, weight in g[v]:
            if ln[w] > ln[v] + weight:
                ln[w] = ln[v] + weight
                X.add(w)


mx = 10 ** 7
g = defaultdict(list)
with open("dijkstraData.txt") as file:
    for line in file:
        if line != "\n":
            lst = [i for i in line.split()]
            for i in lst[1:]:
                x, y = map(int, i.split(","))
                g[int(lst[0])].append((x, y))
ln = [mx] * 201
djk(1)
print(ln)
