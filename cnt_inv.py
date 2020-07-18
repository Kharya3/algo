def merge(a,s, left, right, mid):
    i=left
    k = left
    j=mid+1
    count = 0
    while i<=mid and j<=right:
        if a[i] <= a[j]:
            s[k]=a[i]
            i+=1
        else:
            s[k]=a[j]
            j+=1
            count +=(mid-i+1)
        k+=1

    while j<=right:
        s[k]=a[j]
        j+=1
        k+=1
    while i<=mid:
        s[k]=a[i]
        i+=1
        k+=1
    for i in range(left,right+1):
        a[i]=s[i]
    return count


def merge_sort(a,s, left, right):
    count = 0
    if left<right:
        mid = (left+right)//2
        count += merge_sort(a,s, left, mid)
        count += merge_sort(a,s, mid+1, right)
        count += merge(a,s, left, right, mid)
    return count

f = open("Int_Arr.txt", 'r')
arr = []
for line in f:
    a = line
    a.rstrip()
    arr.append(int(a))
n1 = len(arr)
sorted = [0]*n1
count = merge_sort(arr,sorted, 0, n1-1)
print(count, sorted)
# 2217140747
# n = int(input("n:"))
# l = list(map(int, input("\nEnter the numbers : ").split()))[:n]
# count = merge_sort(l,0,n)
# print(count)
