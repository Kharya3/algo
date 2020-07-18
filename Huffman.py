from myheap import MyMinHeap


class Node(object):
    left = None
    right = None

    def __init__(self, i, w):
        self.item = i
        self.weight = w

    def setChildren(self, ln, rn):
        self.left = ln
        self.right = rn

    def __add__(self, other):
        return self.weight+other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return f"{self.item} - {self.weight} left: {self.left}  right: {self.right}\n"


def codeIt(s, codes, node):
    if node.item:
        if not s:
            codes[node.item] = "0"
        else:
            codes[node.item] = s
    else:
        codeIt(s + "0", codes, node.left)
        codeIt(s + "1", codes, node.right)


def find_element(node, x):
    if node.item == x:
        return True, node.weight
    elif not node.item:
        y = find_element(node.left, x)
        if y[0]: return y
        y = find_element(node.right, x)
        if y[0]: return y
    return False, None


def calculate_depth(node, depth, d):
    if node is None:
        return -1
    if node.left is None and node.right is None:
        # print(node.item)
        return depth
    else:
        l = calculate_depth(node.left, depth + 1, d)
        r = calculate_depth(node.right, depth + 1, d)
        if node.left.item is not None: d[node.left.item] = l
        if node.right.item is not None: d[node.right.item] = r
        # return l + r


def main():
    d = []
    with open("huffman.txt") as file:
        f = file.readlines()
        no = int(f[0])
        for i in range(1, no + 1):
            d.append((i, int(f[i])))
    m = MyMinHeap()
    for i, w in d:
        m.insert(Node(i, w))
    while len(m.Heap) > 2:
        l = m.ext_min()
        r = m.ext_min()
        n = Node(None, l.weight + r.weight)
        n.setChildren(l, r)
        m.insert(n)
    codes = {}
    codeIt("", codes, m.Heap[1])
    e = [-1] * 1001
    calculate_depth(m.Heap[1], 0, e)
    for i in range(1, no +1):
        print(i, e[i], codes[i])
    print(max(e[1:]), min(e[1:]))
    print(m.Heap[1])
    e = [-1] * 1001
    calculate_depth(m.Heap[1], 0, e)


if __name__ == "__main__":
    main()