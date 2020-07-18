class MyMinHeap:

    def __init__(self):
        self.size = 0
        self.Heap = [0]

    def find_min(self):
        return self.Heap[1]

    def insert(self, i):
        self.size += 1
        self.Heap.append(i)
        self.__b_up()

    def __b_up(self):
        i = self.size
        while i // 2:
            if self.Heap[i] < self.Heap[i // 2]:
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
            if self.Heap[i] > self.Heap[min_index]:
                self.Heap[i], self.Heap[min_index] = self.Heap[min_index], self.Heap[i]
                i = min_index
            else:
                break

    def __find_min_child(self, i):
        if 2 * i + 1 > self.size or self.Heap[2 * i] < self.Heap[2 * i + 1]:
            return 2 * i
        else:
            return 2 * i + 1


class MyMaxHeap:

    def __init__(self):
        self.size = 0
        self.Heap = [10 ** 7]

    def find_max(self):
        return self.Heap[1]

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
            max_index = self.__find_max_child(i)
            if self.Heap[i] < self.Heap[max_index]:
                self.Heap[i], self.Heap[max_index] = self.Heap[max_index], self.Heap[i]
                i = max_index
            else:
                break

    def __find_max_child(self, i):
        if 2 * i + 1 > self.size or self.Heap[2 * i] > self.Heap[2 * i + 1]:
            return 2 * i
        else:
            return 2 * i + 1


def signum(a, b):
    if a > b:
        return 1
    elif b > a:
        return -1
    else:
        return 0


def median(arr):
    left = MyMaxHeap()
    right = MyMinHeap()
    ans = 0
    for i in arr:
        s = signum(left.size, right.size)
        if left.size == 0 and right.size == 0:
            left.insert(i)
            med = i
        elif s == 1:
            if i < left.find_max():
                right.insert(left.ext_max())
                left.insert(i)
            else:
                right.insert(i)
            med = left.find_max()
        elif s == -1:
            if i > right.find_min():
                left.insert(right.ext_min())
                right.insert(i)
            else:
                left.insert(i)
            med = left.find_max()
        else:
            if i > right.find_min():
                right.insert(i)
                med = right.find_min()
            else:
                left.insert(i)
                med = left.find_max()
        print(med)
        ans += med
    print(ans)


def main():
    arr = []
    with open("Median.txt") as file:
        for line in file:
            a = line.rstrip().split()
            arr.append(int(*a))
    median(arr)


if __name__ == "__main__":
    main()
