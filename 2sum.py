d = {}
with open("2sum.txt") as file:
    i = 1
    for line in file:
        a = line.rstrip().split()
        d[int(*a)] = i
        i += 1
ans = 0
for t in range(-10000, 10001):
    print((t+10001)*100/20001, "%")
    for i in d.keys():
        j = t - i
        if j in d:
            ans += 1
            break
print(ans)