def maxim(a, left, right):
    if left == right:
        return [a[left]]
    mid = (left + right) // 2
    com1 = maxim(a, left, mid)
    com2 = maxim(a, mid + 1, right)
    if com1[0] > com2[0]:
        com1.append(com2[0])
        return com1
    else:
        com2.append(com1[0])
        return com2


def main():
    a = list(map(int, input("\nEnter the numbers(separate with space;press enter when done):").split()))
    if len(a)<2:
        print("INVALID")
        return
    comp = maxim(a, 0, len(a)-1)
    print("Max is: ", comp[0])
    print(comp)
    comp2 = maxim(comp, 1, len(comp) - 1)
    print("Sec max is: ", comp2[0])
    print(comp2)


if __name__=='__main__':
    main()
