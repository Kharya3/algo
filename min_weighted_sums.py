flag = True
d = {}
lst = []
with open("jobs.txt") as file:
    for line in file:
        if line != "\n":
            w, l = map(int, line.split())
            lst.append((w, l))
lst.sort(reverse=True)
print(lst)
lst1 = sorted(lst, key=lambda x: x[1] - x[0])
lst2 = sorted(lst, key=lambda x: x[1] / x[0])
print(lst1, "\n", lst2)
ans1 = 0
ans2 = 0
length1 = 0
length2 = 0
for i in range(1, 10001):
    length1 += lst1[i - 1][1]
    ans1 += length1 * lst1[i - 1][0]
    length2 += lst2[i - 1][1]
    ans2 += length2 * lst2[i - 1][0]
print(ans1, ans2)
