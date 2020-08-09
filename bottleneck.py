from collections import defaultdict
import sys


class MyMinHeap():

    def __init__(self):
        self.size = 0
        self.Heap = [(0, sys.maxsize)]

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

    def change_key(self, prev_value, new_value):
        index = self.Heap.index(prev_value)
        wgt = new_value[1]
        self.Heap[index][1] = wgt
        self.__b_up(index)


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def bottleneck(self, s):
        S = set()
        dst = [-1*sys.maxsize] * 8
        dst[s] = sys.maxsize
        heap = MyMinHeap()
        for v in self.graph.keys():
            heap.insert([v, dst[v]])
        while heap.size:
            v = heap.ext_min()
            S.add(v[0])
            for w in self.graph[v[0]]:
                distance = min(dst[w[0]], max(dst[v[0]], w[1]))
                if [w[0], dst[w[0]]] in heap.Heap and \
                        distance < dst[w[0]]:
                    temp, dst[w[0]] = dst[w[0]], distance
                    heap.change_key([w[0], temp], [w[0], dst[w[0]]])
        return dst


g = Graph()
with open("s2.txt") as file:
    for line in file:
        if line != "\n":
            lst = [i for i in line.split()]
            for i in lst[1:]:
                x, y = map(int, i.split(","))
                g.graph[int(lst[0])].append([x, y])
# print(g.graph.keys())
dist = g.bottleneck(1)
print(dist)
