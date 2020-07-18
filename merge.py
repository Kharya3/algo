def merge(a, b, c):
    m = len(b)
    l = len(c)
    cnt = 0
    i = j = k = 0
    while i < m and j < l:
        if b[i] <= c[j]:
            a[k] = b[i]
            i+=1
        else:
            a[k] = c[j]
            j+=1
            cnt+=m-i
        k+=1
    while j < l:
        a[k] = c[j]
        j+=1
        k+=1
    while i < m:
        a[k] = b[i]
        i+=1
        k+=1
    return cnt


def merge_sort(a):
    cnt = 0
    if len(a)>1:
        mid = len(a)//2
        b = a[:mid]
        c = a[mid:]
        cnt += merge_sort(b)
        cnt += merge_sort(c)
        cnt += merge(a, b, c)
        b.clear()
        c.clear()
    return cnt


# n = int(input("n:"))
# l = list(map(int, input("\nEnter the numbers : ").split()))[:n]
# cnt = merge_sort(l)
# print(l,"\n",cnt)

f = open("Integer_Array.txt", 'r')
arr = []
for line in f:
    a = line
    a.rstrip()
    arr.append(int(a))
n1 = len(arr)
count = merge_sort(arr)
print(count, arr)
# 2397819672

