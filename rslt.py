import random
import time


def rsl(a, l, r, k):
    if l >= r:
        return l
    x = random.randrange(l, r + 1)
    a[x], a[l] = a[l], a[x]
    pivot = a[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    p = i-1
    a[p], a[l] = a[l], a[p]
    if p-l == k:
        return p
    elif p-l > k:
        return rsl(a, l, p - 1, k)
    return rsl(a, p + 1, r, k - p + l - 1)


def main():
    t = int(input("t: "))
    while t != 0:
        # a = list(map(int, input("\nEnter the numbers(separate with space;press enter when done):").split()))
        a = []
        file = open("Quick_sort.txt", 'r')
        for line in file:
            a.append(int(line))
        i = int(input("i: "))
        s = time.time()
        p=rsl(a, 0, len(a)-1, i-1)
        e = time.time()
        print(a[p], e-s)
        t-=1
        print("")


if __name__ == '__main__':
    main()
