from math import ceil


def Multiply(x,y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    if n%2 == 1:
        n = n+1
    m = n // 2
    p = x // (10 ** m)
    q = x % (10 ** m)
    r = y // (10 ** m)
    s = y % (10 ** m)
    a = Multiply(p, r)
    b = Multiply(q, s)
    c = Multiply(p + q, r + s) - a - b
    return int((10 ** (n)) * a + (10 ** (n//2)) * c + b)


def multiply(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = ceil(n / 2)
    p = x // (10 ** m)
    q = x % (10 ** m)
    r = y // (10 ** m)
    s = y % (10 ** m)
    a = multiply(p, r)
    b = multiply(q, s)
    c = multiply(p + q, r + s) - a - b
    return int((10 ** (2*m)) * a + (10 ** (m)) * c + b)



t = int(input("t:"))
while t!=0:
    input1 = int((input("x:")))
    input2 = int((input("y:")))
    print("m:",multiply(input1, input2))
    print("n:",Multiply(input1, input2))
    t -=1
