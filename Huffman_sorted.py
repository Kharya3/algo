from collections import deque
from Huffman import Node


def find_min(q1, q2):
    if not q1:
        return q2.popleft()
    if not q2:
        return q1.popleft()
    if q1[0] < q2[0]:
        return q1.popleft()
    return q2.popleft()


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


def main():
    d = []
    with open("huffman.txt") as file:
        f = file.readlines()
        no = int(f[0])
        for i in range(1, no + 1):
            d.append((i, int(f[i])))
    d.sort(key=lambda x: x[1])
    print(d)
    q1 = deque()
    q2 = deque()
    print(q1, q2)
    for i, w in d: q1.append(Node(i, w))
    print(q1, q2)
    while q1 or len(q2)> 1:
        l = find_min(q1, q2)
        r = find_min(q1, q2)
        n = Node(None, l+r)
        n.setChildren(l, r)
        q2.append(n)
    print(q2)
    print(q1)
    e = [-1] * 1001
    calculate_depth(q2[0], 0, e)
    print(e)
    print(max(e), min(e[1:]))


if __name__ == "__main__":
    main()
