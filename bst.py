class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


def inorder(root, arr):
    if root is not None:
        inorder(root.left, arr)
        arr.append(root.key)
        inorder(root.right, arr)
    return arr


def main():
    bts = None
    bts = insert(bts, 5)
    bts = insert(bts, 15)
    bts = insert(bts, 53)
    bts = insert(bts, 65)
    bts = insert(bts, 5)

    print(inorder(bts, []))


if __name__ == "__main__":
    main()