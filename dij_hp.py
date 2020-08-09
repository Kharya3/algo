from collections import defaultdict


class MyMinHeap:

    def __init__(self):
        self.size = 0
        self.Heap = [(0, mx)]

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
        self.Heap.pop()
        self.size -= 1
        self.__b_down(1)
        return mn

    def __b_down(self, i):
        while 2 * i <= self.size:
            min_index = self.__find_min_child(i)
            if self.Heap[i][1] > self.Heap[min_index][1]:
                self.Heap[i], self.Heap[min_index] = self.Heap[min_index], self.Heap[i]
                i = min_index
            else:
                break

    def __find_min_child(self, i):
        if 2 * i + 1 > self.size or self.Heap[2 * i][1] < self.Heap[2 * i + 1][1]:
            return 2 * i
        else:
            return 2 * i + 1

    def heapify(self, arr):
        self.size = len(arr)
        self.Heap += arr
        for i in range(self.size // 2, -1, -1):
            self.__b_down(i)

    def pr_heap(self):
        for i in range(1, self.size // 2 + 1):
            if i == self.size // 2 and 2 * i + 1 > self.size:
                print(self.Heap[i], "---", self.Heap[2 * i])
                break
            print(self.Heap[i], "---", self.Heap[2 * i], ", ", self.Heap[2 * i + 1])

    def change_key(self, new_value, prev_value):
        index = self.Heap.index(prev_value)
        wgt = new_value[1]
        self.Heap[index][1] = wgt
        self.__b_up(index)


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def djk(self, s):
        X = []
        key = [mx]*201
        key[s] = 0
        heap = MyMinHeap()
        for v in self.graph.keys():
            heap.insert([v, key[v]])
        while heap.size:
            w = heap.ext_min()
            X.append(w[0])
            for v in self.graph[w[0]]:
                if [v[0], key[v[0]]] in heap.Heap and key[w[0]] != mx and \
                        v[1]+key[w[0]] < key[v[0]]:
                    temp, key[v[0]] = key[v[0]], key[w[0]]+v[1]
                    heap.change_key([v[0], key[v[0]]], [v[0], temp])
        print(X)
        return key


mx = 10 ** 7
g = Graph()
with open("dijkstraData.txt") as file:
    for line in file:
        if line != "\n":
            lst = [i for i in line.split()]
            for i in lst[1:]:
                x, y = map(int, i.split(","))
                g.graph[int(lst[0])].append([x, y])
k = g.djk(1)
print(k)
