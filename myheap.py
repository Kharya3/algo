class MyMinHeap:

    def __init__(self):
        self.size = 0
        self.Heap = [0]

    def insert(self, i):
        self.size += 1
        self.Heap.append(i)
        self.__b_up(self.size)

    def __b_up(self, i):
        while i // 2:
            if self.Heap[i] < self.Heap[i // 2]:
                self.Heap[i], self.Heap[i // 2] = self.Heap[i // 2], self.Heap[i]
                i //= 2
            else:
                break

    def ext_min(self):
        mn = self.Heap[1]
        self.Heap[1] = self.Heap[-1]
        r = self.Heap.pop()
        self.size -= 1
        self.__b_down(1)
        return mn

    def __b_down(self, i):
        while 2 * i <= self.size:
            min_index = self.find_min_child(i)
            if self.Heap[i] > self.Heap[min_index]:
                self.Heap[i], self.Heap[min_index] = self.Heap[min_index], self.Heap[i]
                i = min_index
            else:
                break

    def find_min_child(self, i):
        if 2 * i + 1 > self.size or self.Heap[2 * i] < self.Heap[2 * i + 1]:
            return 2 * i
        else:
            return 2 * i + 1

    def heapify(self, arr):
        self.size = len(arr)
        self.Heap += arr
        for i in range(self.size // 2, -1, -1):
            self.__b_down(i)

    def delete(self, x):
        index = self.Heap.index(x)
        self.Heap[index] = self.Heap[-1]
        self.Heap.pop()
        self.size -= 1
        self.__b_down(index)

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


# mmh = MyMinHeap()
# arr = [82, 67, 73, 3, 9, 2, 11, 34, 78, 90, 12, 23, 45, 89]
# mmh.heapify(arr)
# print(mmh.Heap[1:])
# mmh.pr_heap()
# mmh.delete(11)
# print(mmh.Heap[1:])
# mmh.pr_heap()
# a = MyMinHeap()
# a.insert(2)
# a.insert(3)
# a.insert(6)
# a.insert(23)
# a.insert(53)
# a.insert(77)
# print(a.Heap[1:])
# a.delete(23)
# print(a.Heap[1:])
# print(a.ext_min())
# print(a.Heap[1:])
# a.pr_heap()


class MyMaxHeap:

    def __init__(self):
        self.size = 0
        self.Heap = [10 ** 7]

    def insert(self, i):
        self.size += 1
        self.Heap.append(i)
        self.__b_up()

    def __b_up(self):
        i = self.size
        while i // 2:
            if self.Heap[i] > self.Heap[i // 2]:
                self.Heap[i], self.Heap[i // 2] = self.Heap[i // 2], self.Heap[i]
                i //= 2
            else:
                break

    def ext_max(self):
        mx = self.Heap[1]
        self.Heap[1] = self.Heap[self.size]
        self.Heap.pop()
        self.size -= 1
        self.__b_down(1)
        return mx

    def __b_down(self, i):
        while 2 * i <= self.size:
            max_index = self.find_max_child(i)
            if self.Heap[i] < self.Heap[max_index]:
                self.Heap[i], self.Heap[max_index] = self.Heap[max_index], self.Heap[i]
                i = max_index
            else:
                break

    def find_max_child(self, i):
        if 2 * i + 1 > self.size or self.Heap[2 * i] > self.Heap[2 * i + 1]:
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

# mmh = MyMaxHeap()
# arr = [82, 67, 73, 3, 9, 2, 11, 34, 78, 90, 12, 23, 45, 89]
# mmh.heapify(arr)
# print(mmh.Heap[1:])
# mmh.pr_heap()
# a = MyMaxHeap()
# a.insert(2)
# a.insert(3)
# a.insert(6)
# a.insert(23)
# a.insert(53)
# a.insert(77)
# print(a.Heap[1:])
# print(a.ext_max())
# print(a.Heap[1:])
# a.pr_heap()
