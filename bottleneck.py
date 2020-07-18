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
# 662, 652, 953, 701, 1229, 662, 730, 647, 807, 647, 700, 861, 700, 809, 839, 1275, 700, 647, 647, 1229, 1332, 897, 1332, 821, 647, 714, 1724, 1005, 647, 953, 1615, 647, 662, 508, 634, 648, 1369, 853, 2199, 761, 647, 1171, 647, 701, 1229, 1229, 761, 953, 861, 701, 561, 662, 953, 771, 647, 810, 1050, 761, 701, 647, 662, 1315, 647, 647, 777, 700, 2277, 824, 647, 647, 647, 761, 1223, 647, 1079, 561, 761, 647, 647, 700, 647, 1332, 647, 517, 647, 647, 1369, 1723, 928, 561, 647, 2349, 810, 647, 647, 1883, 980, 761, 647, 1393, 1172, 696, 992, 624, 647, 701, 648, 701, 696, 785, 647, 652, 508, 983, 810, 1399, 700, 647, 700, 771, 714, 1229, 647, 647, 648, 1402, 647, 508, 730, 700, 821, 836, 647, 647, 1320, 1096, 700, 1235, 546, 647, 700, 821, 652, 648, 820, 1087, 700, 1003, 634, 1332, 1087, 647, 700, 648, 771, 647, 647, 647, 561, 1726, 761, 647, 647, 897, 2364, 820, 899, 701, 647, 1394, 992, 647, 1723, 714, 1128, 1332, 730, 664, 624, 701, 953, 647, 647, 700, 1324, 647, 647, 1115, 697, 1403, 544, 1229, 647, 647, 647, 751, 1724, 647, 700