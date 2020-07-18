from collections import defaultdict
from sys import maxsize
# from myheap import MyMinHeap as mmh

class mmh:

    def __init__(self):
        self.size = 0
        self.Heap = [[0, 0]]

    def insert(self, i):
        self.size += 1
        self.Heap.append(i)
        self.__b_up(self.size)

    def __b_up(self, i):
        while i // 2:
            if self.Heap[i][1] < self.Heap[i // 2][1]:
                self.Heap[i], self.Heap[i // 2] = self.Heap[i // 2], self.Heap[i]
                i //= 2
            else:
                break

    def ext_min(self):
        mn = self.Heap[1]
        self.Heap[1] = self.Heap[self.size]
        r = self.Heap.pop()
        self.size -= 1
        self.__b_down(1)
        return mn

    def __b_down(self, i):
        while 2 * i <= self.size:
            min_index = self.find_min_child(i)
            if self.Heap[i][1] > self.Heap[min_index][1]:
                self.Heap[i], self.Heap[min_index] = self.Heap[min_index], self.Heap[i]
                i = min_index
            else:
                break

    def find_min_child(self, i):
        if 2 * i + 1 > self.size or self.Heap[2 * i][1] < self.Heap[2 * i + 1][1]:
            return 2 * i
        else:
            return 2 * i + 1

    def heapify(self, arr):
        self.size = len(arr)
        self.Heap += arr
        for i in range(self.size // 2, -1, -1):
            self.__b_down(i)

    def change_key(self, wgt, prev_value):
        index = self.Heap.index(prev_value)
        self.Heap[index][1] = wgt
        self.__b_up(index)

    def pr_heap(self):
        for i in range(1, self.size // 2 + 1):
            if i == self.size // 2 and 2 * i + 1 > self.size:
                print(self.Heap[i], "---", self.Heap[2 * i])
                break
            print(self.Heap[i], "---", self.Heap[2 * i], ", ", self.Heap[2 * i + 1])


def takeInp():
    g = defaultdict(list)
    with open("edges.txt") as file:
        f = file.readlines()
        n, m = map(int, f[0].split())
        for i in range(1, m + 1):
            v1, v2, c = map(int, f[i].split())
            g[v1].append((v2, c))
            g[v2].append((v1, c))
    return g, n, m


def main():
    g, n, m = takeInp()
    s = 1
    X = {s}
    T = []
    heap = mmh()
    key = [maxsize] * (n + 1)
    winner = [None] * (n + 1)
    for v, c in g[s]:
        key[v] = c
        winner[v] = (s, v, c)
    for v in g.keys():
        if v is not s:
            heap.insert([v, key[v]])
    while heap.size:
        w, c1 = heap.ext_min()
        X.add(w)
        T.append(winner[w])
        for y, c in g[w]:
            if y not in X and c < key[y]:
                heap.change_key(c, [y, key[y]])
                key[y] = c
                winner[y] = (w, y, c)
    print(sum(i[2] for i in T))


if __name__ == "__main__":
    main()
