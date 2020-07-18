from collections import defaultdict


# def find_min(w):
#     return min(w, key=lambda x: x[1])


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
print(ln[7], ln[37], ln[59], ln[82], ln[99], ln[115], ln[133], ln[165], ln[188], ln[197])
# 2599 2610 2947 2052 2367 2399 2029 2442 2505 3068