import random


def med_3(a, l, h):
    m = (l+h)//2
    if a[m] < a[l]:
        if a[l] < a[h]:
            return l
        if a[h] < a[m]:
            return m
        return h
    else:
        if a[m] < a[h]:
            return m
        if a[h] < a[l]:
            return l
        return h


def qui_srt(a, low, high):
    cnt = 0
    if high <= low:
        return cnt
    cnt += high-low
    # med = med_3(a, low, high)
    # a[low], a[med] = a[med], a[low]
    x = random.randrange(low, high + 1)
    a[x], a[low] = a[low], a[x]
    pivot = a[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i - 1], a[low] = a[low], a[i - 1]
    cnt +=qui_srt(a, low, i - 2)
    cnt +=qui_srt(a, i, high)
    return cnt


def main():
    file = open("Quick_sort.txt", 'r')
    arr = []
    for line in file:
        arr.append(int(line))
    # arr = list(map(int, input("\nEnter the numbers(separate with space;press enter when done):").split()))
    cnt = qui_srt(arr, 0, len(arr) - 1)
    print(cnt)
    print(arr)


if __name__ == '__main__':
    main()
# a[0] =
# a[high] = 164123
#  med = 138382
