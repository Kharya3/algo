from math import sqrt


def sort_y(t):
    return t[1]


def sort_x(t):
    return t[0]


def distance(x, y):
    d_x = x[0] - y[0]
    d_y = x[1] - y[1]
    return sqrt((d_x ** 2) + (d_y ** 2))


def brute_search(a):
    ln = len(a)
    least = distance(a[0], a[1])
    m1 = a[0], a[1]
    if ln is 2:
        return m1,  least
    for i in range(ln - 1):
        for j in range(i + 1, ln - 1):
            dis = distance(a[i], a[j])
            if dis < least:
                least = dis
                m1 = a[i], a[j]
    return m1, least


def split(px, py, dl, p):
    mid = len(px) // 2
    x_bar = px[mid][0]
    sy = [point for point in py if x_bar - dl < point[0] < x_bar + dl]
    ln = len(sy)
    for i in range(1, ln - 1):
        for j in range(1, min(7, ln - i)):
            dis = distance(sy[i], sy[i + j])
            if dis < dl:
                dl = dis
                p = sy[i], sy[i + j]
    return p, dl


def solve(px, py):
    if len(px) <= 3:
        return brute_search(px)
    mid = len(px) // 2
    lx = px[:mid]  # first half of px sorted by x coor
    rx = px[mid:]  # second half of px sorted by x coor
    ly = sorted(lx, key=sort_y)  # first half of px sorted by y coor
    ry = sorted(rx, key=sort_y)  # second half of px sorted by y coor
    p1, min1 = solve(lx, ly)
    p2, min2 = solve(rx, ry)
    if min1 < min2:
        delta = min1
    else:
        delta = min2
        p1 = p2
    p3, min3 = split(px, py, delta, p1)
    if delta < min3:
        return p1, delta
    else:
        return p3, min3



t = list(tuple(map(int, input().split())) for r in range(int(input('enter no of rows : '))))
px = sorted(t, key=sort_x)  # coordinates sorted by x coordinate
py = sorted(t, key=sort_y)  # coordinates sorted by y coordinate
p, least = solve(px, py)
print(least, p)
