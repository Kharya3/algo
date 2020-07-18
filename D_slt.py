from math import ceil
import random

def main():
    arr = random.sample(range(0, 100), 100)
    for _ in range(int(input())):
        k = int(input())
        a = dSelect(arr,0,len(arr)-1, k)
        print(arr)
        print(arr[a])


def dSelect(a,l,r, k):
    print(a)
    n = r-l+1
    if n == 1:
        return l
    c = []
    h = 0
    while h<n:
        temp = []
        j = 0
        while h < n and j<5:
            temp.append(a[h])
            h += 1
            j+=1
        temp.sort()
        c.append(temp[len(temp)//2])
        temp.clear()
    c.sort()
    x = c[len(c)//2]
    a[x], a[l] = a[l], a[x]
    pivot = a[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    p = i - 1
    a[p], a[l] = a[l], a[p]
    if p - l == k:
        return p
    elif p - l > k:
        return dSelect(a, l, p - 1, k)
    return dSelect(a, p + 1, r, k - p + l - 1)


def merge(a, b, c):
    m = len(b)
    l = len(c)
    i = j = k = 0
    while i < m and j < l:
        if b[i] <= c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        k += 1
    while j < l:
        a[k] = c[j]
        j += 1
        k += 1
    while i < m:
        a[k] = b[i]
        i += 1
        k += 1


def merge_sort(a):
    mid = len(a) // 2
    if len(a) > 1:
        b = a[:mid]
        c = a[mid:]
        merge_sort(b)
        merge_sort(c)
        merge(a, b, c)
        b.clear()
        c.clear()
        return a[mid]
    return a[0]


if __name__ == '__main__':
    main()
