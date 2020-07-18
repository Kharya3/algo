class UnionFind(object):

    def __init__(self, arr=None):
        self.arr = []
        self.parent = []
        self.size = []
        self.n_comp = 0
        if arr:
            for x in arr: self.add(x)

    def add(self, x):
        if x not in self:
            self.arr.append(x)
            self.parent.append(self.arr.index(x))
            self.size.append(1)
            self.n_comp += 1

    def __len__(self):
        return len(self.arr)

    def __contains__(self, x):
        return x in self.arr

    def find(self, x):
        ind = self.arr.index(x)
        while ind != self.parent[ind]:
            ind = self.parent[ind]
        return ind

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root: return
        if self.size[x_root] > self.size[y_root]:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
        else:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        self.n_comp -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
